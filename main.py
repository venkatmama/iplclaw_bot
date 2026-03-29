import os
import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from anthropic import Anthropic

from sportradar_api import get_live_match, fetch_timeline
from player_prices import AUCTION_PRICES

# ─── CONFIG ─────────────────────────────────────────────
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

POLL_INTERVAL = 2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("IPLClaw-Pro")

client = Anthropic(api_key=ANTHROPIC_API_KEY)

subscribed_chats = set()
last_event_id = None
player_stats = {}
current_match_id = None

# ─── NAME MATCH FIX ─────────────────────────────────────
def get_player_data(name):
    if name in AUCTION_PRICES:
        return AUCTION_PRICES[name]

    for p in AUCTION_PRICES:
        if name.lower() in p.lower():
            return AUCTION_PRICES[p]

    return None

# ─── PROCESS EVENT ─────────────────────────────────────
def process_event(event):
    etype = event.get("type")

    if etype not in ["delivery", "wicket"]:
        return None

    batsman = event.get("player", {}).get("name")
    bowler = event.get("bowler", {}).get("name")
    runs = event.get("runs", 0)
    over = event.get("over")

    if not batsman:
        return None

    if batsman not in player_stats:
        player_stats[batsman] = {"runs": 0, "balls": 0}

    player_stats[batsman]["runs"] += runs
    player_stats[batsman]["balls"] += 1

    return {
        "type": etype,
        "batsman": batsman,
        "bowler": bowler,
        "runs": runs,
        "over": over
    }

# ─── ROI ───────────────────────────────────────────────
def calculate_roi(player):
    data = get_player_data(player)

    if not data:
        return "N/A", "Unknown 🤷"

    runs = player_stats[player]["runs"]
    price = data["price_cr"]

    per_match_lakh = (price / 14) * 100

    if runs == 0:
        return "∞", "SCAM 💀"

    cost = round(per_match_lakh / runs, 1)

    if runs >= 50:
        verdict = "MEGA STEAL 🤑"
    elif runs >= 30:
        verdict = "PAISA WASOOL ✅"
    elif runs >= 15:
        verdict = "OVERPRICED 😬"
    else:
        verdict = "FLOP 💀"

    return cost, verdict

# ─── AI ROAST ──────────────────────────────────────────
SYSTEM_PROMPT = """
You are IPLClaw 💀 savage IPL commentator.

Rules:
- Hinglish
- Max 2 lines
- Roast using price vs performance
- Funny, brutal, meme style
"""

async def generate_roast(prompt):
    try:
        res = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=100,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}]
        )
        return res.content[0].text
    except:
        return "Roast failed 💀"

# ─── MESSAGE BUILDER ───────────────────────────────────
async def build_message(event):
    batsman = event["batsman"]
    bowler = event["bowler"]
    runs = event["runs"]
    over = event["over"]
    etype = event["type"]

    data = get_player_data(batsman)
    price = data["price_cr"] if data else "unknown"

    cost, verdict = calculate_roi(batsman)

    # WICKET ROAST
    if etype == "wicket":
        prompt = f"""
        {batsman} OUT
        Runs: {player_stats[batsman]['runs']}
        Price: ₹{price} Cr

        Roast brutally. Mention waste of money.
        """

        roast = await generate_roast(prompt)

        return f"""🚨 WICKET {over}

{batsman} OUT 💀

💀 {roast}

💰 Cost/run: ₹{cost} lakh
Verdict: {verdict}
"""

    # NORMAL BALL
    else:
        prompt = f"""
        Over {over}
        {batsman} vs {bowler}
        Runs: {runs}
        Price: ₹{price} Cr

        Roast performance vs price.
        """

        roast = await generate_roast(prompt)

        return f"""🏏 {over} {batsman} - {runs}

💀 {roast}

💰 Cost/run: ₹{cost} lakh
Verdict: {verdict}
"""

# ─── COMMANDS ───────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💀 IPL PRO LIVE...\n\nThis is just for fun, so no hard feelings..\n\nI beleive you will enjoy it very much.../subscribe to start roasting"
    )

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subscribed_chats.add(update.effective_chat.id)
    await update.message.reply_text("🔥 Subscribed")

async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subscribed_chats.discard(update.effective_chat.id)
    await update.message.reply_text("Stopped")

# ─── POLLING ───────────────────────────────────────────
async def poll(app):
    global last_event_id, current_match_id

    bot = app.bot

    while True:
        try:
            if not subscribed_chats:
                await asyncio.sleep(POLL_INTERVAL)
                continue

            if not current_match_id:
                current_match_id = await get_live_match()
                print("Match ID:", current_match_id)
                await asyncio.sleep(3)
                continue

            data = await fetch_timeline(current_match_id)
            events = data.get("timeline", [])

            if not events:
                await asyncio.sleep(POLL_INTERVAL)
                continue

            latest = events[-1]
            event_id = latest.get("id")

            if event_id != last_event_id:
                last_event_id = event_id

                processed = process_event(latest)

                if processed:
                    msg = await build_message(processed)

                    for chat_id in subscribed_chats:
                        await bot.send_message(chat_id=chat_id, text=msg)

        except Exception as e:
            logger.error(e)

        await asyncio.sleep(POLL_INTERVAL)

# ─── MAIN ──────────────────────────────────────────────
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("subscribe", subscribe))
    app.add_handler(CommandHandler("unsubscribe", unsubscribe))

    async def on_start(app):
        asyncio.create_task(poll(app))

    app.post_init = on_start

    print("🔥 IPLClaw PRO RUNNING...")
    app.run_polling()

if __name__ == "__main__":
    main()
