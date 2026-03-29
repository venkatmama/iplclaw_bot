import os
import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import httpx
from anthropic import Anthropic

from player_prices import AUCTION_PRICES

# ─── CONFIG ─────────────────────────────────────────────
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CRICKET_API_KEY = os.getenv("CRICKET_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

POLL_INTERVAL = 8

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("IPLClaw")

client = Anthropic(api_key=ANTHROPIC_API_KEY)

subscribed_chats = set()
last_state = {}

# ─── FETCH LIVE MATCH ───────────────────────────────────
async def fetch_live_match():
    url = f"https://api.cricapi.com/v1/currentMatches?apikey={CRICKET_API_KEY}&offset=0"
    async with httpx.AsyncClient() as http:
        res = await http.get(url, timeout=10)
        data = res.json()

    for match in data.get("data", []):
        if "IPL" in match.get("series", ""):
            return match
    return None

# ─── AI ROAST ───────────────────────────────────────────
SYSTEM_PROMPT = """
You are IPLClaw 💀 — savage IPL commentator.

Rules:
- Roast players using auction price vs performance
- Use Hinglish (bhai, paisa vasool, kya kar raha hai)
- Max 2 lines
- Brutal + funny
- Use emojis: 💀🔥🤡🤑😭
"""

async def generate_roast(prompt):
    try:
        msg = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=120,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}]
        )
        return msg.content[0].text
    except Exception as e:
        logger.error(e)
        return "Roast engine broke 💀"

# ─── EVENT DETECTION ────────────────────────────────────
def detect_events(old, new):
    events = []
    if not old or not new:
        return events

    try:
        o = old["score"][0]
        n = new["score"][0]

        old_runs, new_runs = o["r"], n["r"]
        old_w, new_w = o["w"], n["w"]
        old_ov, new_ov = float(o["o"]), float(n["o"])

        if new_ov > old_ov:
            events.append({"type": "ball", "runs": new_runs - old_runs})

        if int(new_ov) > int(old_ov):
            events.append({"type": "over", "runs": new_runs - old_runs})

        if new_w > old_w:
            events.append({"type": "wicket"})

    except:
        pass

    return events

# ─── COMMANDS ───────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏏💀 IPLClaw LIVE\n\n"
        "/subscribe → live roasts\n"
        "/live → current score"
    )

async def live(update: Update, context: ContextTypes.DEFAULT_TYPE):
    match = await fetch_live_match()
    if not match:
        await update.message.reply_text("No live IPL match")
        return

    s = match["score"][0]
    msg = f"{match['name']}\n{s['r']}/{s['w']} ({s['o']})\n{match['status']}"
    await update.message.reply_text(msg)

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subscribed_chats.add(update.effective_chat.id)
    await update.message.reply_text("Subscribed 🔥")

async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subscribed_chats.discard(update.effective_chat.id)
    await update.message.reply_text("Unsubscribed")

# ─── POLLING ENGINE ─────────────────────────────────────
async def poll(app):
    global last_state
    bot = app.bot

    while True:
        try:
            if not subscribed_chats:
                await asyncio.sleep(POLL_INTERVAL)
                continue

            match = await fetch_live_match()
            if not match:
                await asyncio.sleep(POLL_INTERVAL)
                continue

            events = detect_events(last_state, match)

            for event in events:

                if event["type"] == "ball":
                    roast = await generate_roast(
                        f"Ball happened. Runs: {event['runs']}. Roast batsman or bowler based on price."
                    )
                    msg = f"🏏 BALL\n💀 {roast}"

                elif event["type"] == "over":
                    roast = await generate_roast(
                        f"Over completed. Runs: {event['runs']}. Compare performance vs auction price."
                    )
                    msg = f"🔥 OVER\n💀 {roast}"

                elif event["type"] == "wicket":
                    roast = await generate_roast(
                        "Wicket fell. Roast batsman for wasting auction money."
                    )
                    msg = f"🚨 WICKET\n💀 {roast}"

                else:
                    continue

                for chat_id in subscribed_chats:
                    await bot.send_message(chat_id=chat_id, text=msg)

            last_state = match

        except Exception as e:
            logger.error(e)

        await asyncio.sleep(POLL_INTERVAL)

# ─── MAIN ───────────────────────────────────────────────
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("live", live))
    app.add_handler(CommandHandler("subscribe", subscribe))
    app.add_handler(CommandHandler("unsubscribe", unsubscribe))

    loop = asyncio.get_event_loop()
    loop.create_task(poll(app))

    print("🔥 BOT RUNNING...")
    app.run_polling()

if __name__ == "__main__":
    main()