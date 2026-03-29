import os
import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from anthropic import Anthropic

from sportradar_api import fetch_ball_data
from player_prices import AUCTION_PRICES

# ─── CONFIG ─────────────────────────────────────────────
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

POLL_INTERVAL = 2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("IPLClaw")

client = Anthropic(api_key=ANTHROPIC_API_KEY)

subscribed_chats = set()
last_event_id = None
player_stats = {}

# ─── PROCESS BALL ──────────────────────────────────────
def process_event(event):
    if event.get("type") != "delivery":
        return None

    batsman = event["player"]["name"]
    bowler = event["bowler"]["name"]
    runs = event.get("runs", 0)
    over = event.get("over")

    if batsman not in player_stats:
        player_stats[batsman] = {"runs": 0, "balls": 0}

    player_stats[batsman]["runs"] += runs
    player_stats[batsman]["balls"] += 1

    return batsman, bowler, runs, over

# ─── ROI CALCULATION ───────────────────────────────────
def calculate_roi(player):
    data = AUCTION_PRICES.get(player)

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
You are IPLClaw 💀 savage commentator.

Rules:
- Hinglish
- Max 2 lines
- Roast using price vs performance
- Funny + brutal
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

# ─── BUILD MESSAGE ─────────────────────────────────────
async def build_message(batsman, bowler, runs, over):
    price = AUCTION_PRICES.get(batsman, {}).get("price_cr", "unknown")
    cost, verdict = calculate_roi(batsman)

    prompt = f"""
    Over {over}
    {batsman} vs {bowler}
    Runs: {runs}
    Price: ₹{price} Cr

    Roast this moment and judge paisa vasool.
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
        "🏏💀 IPLClaw LIVE\n\n/subscribe to start"
    )

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subscribed_chats.add(update.effective_chat.id)
    await update.message.reply_text("Subscribed 🔥")

async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subscribed_chats.discard(update.effective_chat.id)
    await update.message.reply_text("Stopped")

# ─── POLLING ───────────────────────────────────────────
async def poll(app):
    global last_event_id
    bot = app.bot

    while True:
        try:
            if not subscribed_chats:
                await asyncio.sleep(POLL_INTERVAL)
                continue

            data = await fetch_ball_data()

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
                    batsman, bowler, runs, over = processed
                    msg = await build_message(batsman, bowler, runs, over)

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

    print("🔥 Sportradar Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
