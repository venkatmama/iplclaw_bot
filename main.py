import os
import asyncio
import logging
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, ContextTypes,
    MessageHandler, filters, PreCheckoutQueryHandler
)
from anthropic import Anthropic

from sportradar_api import get_live_match, fetch_timeline
from player_prices import AUCTION_PRICES
from payments import PREMIUM_TITLE, PREMIUM_DESC, get_prices
from storage import start_trial, activate_paid, is_premium, has_used_trial

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("IPLClaw")

client = Anthropic(api_key=ANTHROPIC_API_KEY)

live_chats = set()
player_stats = {}
last_event_id = None
current_match_id = None

# ─── START ─────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not has_used_trial(user_id):
        start_trial(user_id)
        msg = "🔥 1 DAY FREE TRIAL STARTED\n\nUse /live"
    else:
        msg = "Welcome back 💀\nUse /live or /premium"

    await update.message.reply_text(msg)

# ─── PAYMENT ───────────────────────────────────────────
async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_invoice(
        title=PREMIUM_TITLE,
        description=PREMIUM_DESC,
        payload="lifetime",
        provider_token="",
        currency="XTR",
        prices=get_prices(),
        start_parameter="premium"
    )

async def precheckout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.pre_checkout_query.answer(ok=True)

async def successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    activate_paid(user_id)

    await update.message.reply_text("🔥 Lifetime Activated 💀")

# ─── LIVE COMMAND ──────────────────────────────────────
async def live(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not is_premium(user_id):
        await update.message.reply_text(
            "💀 Trial expired\nUse /premium to continue"
        )
        return

    live_chats.add(update.effective_chat.id)
    await update.message.reply_text("🔥 Live updates started 💀")

# ─── EVENT PROCESS ─────────────────────────────────────
def process_event(event):
    if event.get("type") != "delivery":
        return None

    player = event.get("player", {}).get("name")
    runs = event.get("runs", 0)

    if not player:
        return None

    if player not in player_stats:
        player_stats[player] = {"runs": 0}

    player_stats[player]["runs"] += runs

    return player, runs

# ─── POLLING ───────────────────────────────────────────
async def poll(app):
    global last_event_id, current_match_id

    bot = app.bot

    while True:
        try:
            if not live_chats:
                await asyncio.sleep(2)
                continue

            if not current_match_id:
                current_match_id = await get_live_match()
                await asyncio.sleep(3)
                continue

            data = await fetch_timeline(current_match_id)
            events = data.get("timeline", [])

            if not events:
                await asyncio.sleep(2)
                continue

            latest = events[-1]
            event_id = latest.get("id")

            if event_id != last_event_id:
                last_event_id = event_id

                processed = process_event(latest)

                if processed:
                    player, runs = processed

                    msg = f"🏏 {player} scored {runs} 💀"

                    for chat_id in live_chats:
                        await bot.send_message(chat_id=chat_id, text=msg)

        except Exception as e:
            logger.error(e)

        await asyncio.sleep(2)

# ─── MAIN ──────────────────────────────────────────────
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("live", live))
    app.add_handler(CommandHandler("premium", premium))

    app.add_handler(PreCheckoutQueryHandler(precheckout))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment))

    async def on_start(app):
        asyncio.create_task(poll(app))

    app.post_init = on_start

    print("🔥 IPLClaw LIVE RUNNING")
    app.run_polling()

if __name__ == "__main__":
    main()
