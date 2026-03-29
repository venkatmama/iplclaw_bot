import os
import asyncio
import logging
import httpx
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from anthropic import Anthropic

from player_prices import AUCTION_PRICES

# ─── CONFIG ─────────────────────────────────────────────
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# ⚠️ Replace with LIVE IPL match ID (update manually for now)
MATCH_ID = "ipl_match_id_here"

POLL_INTERVAL = 3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("IPLClaw")

client = Anthropic(api_key=ANTHROPIC_API_KEY)

subscribed_chats = set()
last_ball_id = None
player_stats = {}

# ─── FETCH CRICBUZZ COMMENTARY ─────────────────────────
async def fetch_commentary():
    url = f"https://www.cricbuzz.com/api/cricket-match/commentary/{MATCH_ID}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    async with httpx.AsyncClient() as http:
        res = await http.get(url, headers=headers)
        return res.json()

# ─── PROCESS BALL ──────────────────────────────────────
def process_ball(ball):
    batsman = ball.get("batsmanName")
    bowler = ball.get("bowlerName")
    runs = ball.get("runs", 0)
    over = ball.get("overNumber")

    if not batsman:
        return None

    if batsman not in player_stats:
        player_stats[batsman] = {"runs": 0, "balls": 0}

    player_stats[batsman]["runs"] += runs
    player_stats[batsman]["balls"] += 1

    return batsman, bowler, runs, over

# ─── ROI CALCULATION ───────────────────────────────────
def calculate_roi(player):
    data = AUCTION_PRICES.get(player)

    if not data:
        return None, "Unknown 🤷"

    runs = player_stats[player]["runs"]
    price = data["price_cr"]

    per_match_lakh = (price / 14) * 100

    if runs == 0:
        return "∞", "DAYLIGHT ROBBERY 💀"

    cost_per_run = round(per_match_lakh / runs, 1)

    if runs >= 50:
        verdict = "MEGA STEAL 🤑"
    elif runs >= 30:
        verdict = "PAISA WASOOL ✅"
    elif runs >= 15:
        verdict = "OVERPRICED 😬"
    else:
        verdict = "FLOP SHOW 💀"

    return cost_per_run, verdict

# ─── AI ROAST ──────────────────────────────────────────
SYSTEM_PROMPT = """
You are IPLClaw 💀 — savage IPL commentator.

Rules:
- Roast players using auction price vs performance
- Use Hinglish
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

# ─── BALL ROAST BUILDER ────────────────────────────────
async def build_message(batsman, bowler, runs, over):
    price = AUCTION_PRICES.get(batsman, {}).get("price_cr", "unknown")

    cost, verdict = calculate_roi(batsman)

    prompt = f"""
    Over {over}
    {batsman} vs {bowler}
    Runs: {runs}
    Price: ₹{price} Cr

    Roast this moment in IPL match.
    Compare performance vs price.
    """

    roast = await generate_roast(prompt)

    return f"""🏏 {over} {batsman} - {runs} run

💀 {roast}

💰 Cost/run: ₹{cost} lakh
Verdict: {verdict}
"""

# ─── TELEGRAM COMMANDS ─────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏏💀 IPLClaw LIVE\n\n"
        "/subscribe → ball-by-ball roasting\n"
        "/unsubscribe → stop"
    )

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subscribed_chats.add(update.effective_chat.id)
    await update.message.reply_text("🔥 Subscribed — chaos incoming 💀")

async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subscribed_chats.discard(update.effective_chat.id)
    await update.message.reply_text("Stopped updates")

# ─── POLLING LOOP ──────────────────────────────────────
async def poll(app):
    global last_ball_id

    bot = app.bot

    while True:
        try:
            if not subscribed_chats:
                await asyncio.sleep(POLL_INTERVAL)
                continue

            data = await fetch_commentary()

            balls = data.get("commentaryList", [])

            if not balls:
                await asyncio.sleep(POLL_INTERVAL)
                continue

            latest = balls[0]
            ball_id = latest.get("commId")

            if ball_id != last_ball_id:
                last_ball_id = ball_id

                processed = process_ball(latest)

                if processed:
                    batsman, bowler, runs, over = processed

                    msg = await build_message(
                        batsman, bowler, runs, over
                    )

                    for chat_id in subscribed_chats:
                        await bot.send_message(chat_id=chat_id, text=msg)

        except Exception as e:
            logger.error(f"Polling error: {e}")

        await asyncio.sleep(POLL_INTERVAL)

# ─── MAIN ──────────────────────────────────────────────
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("subscribe", subscribe))
    app.add_handler(CommandHandler("unsubscribe", unsubscribe))

    # Start background polling task
    app.job_queue.run_once(lambda ctx: asyncio.create_task(poll(app)), 0)

    print("🔥 BOT RUNNING ON RAILWAY...")
    app.run_polling()
