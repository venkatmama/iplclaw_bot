import os
import asyncio
import logging
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, ContextTypes,
    MessageHandler, filters, PreCheckoutQueryHandler
)
from anthropic import Anthropic

from sportradar_api import get_match, fetch_timeline
from db import create_table, add_user, activate_paid, is_premium
from payments import get_prices

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=ANTHROPIC_API_KEY)

logging.basicConfig(level=logging.INFO)

live_chats = set()
last_event_id = None
player_stats = {}

# ─── AI ROAST ──────────────────────────────────────────
async def generate_roast(player, runs):
    try:
        prompt = f"{player} scored {runs}. Roast based on IPL price vs performance."
        res = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=80,
            messages=[{"role": "user", "content": prompt}]
        )
        return res.content[0].text
    except:
        return "💀 performance speaks for itself"

# ─── START ─────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    add_user(user_id)

    await update.message.reply_text(
        "🔥 1-day trial started\n\nUse /live"
    )

# ─── LIVE ──────────────────────────────────────────────
async def live(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not is_premium(user_id):
        await update.message.reply_text("💀 Trial expired → /premium")
        return

    live_chats.add(update.effective_chat.id)
    await update.message.reply_text("🔥 Live started")

# ─── PAYMENT ───────────────────────────────────────────
async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_invoice(
        title="IPLClaw Lifetime 💀",
        description="Full access",
        payload="premium",
        provider_token="",
        currency="XTR",
        prices=get_prices()
    )

async def precheckout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.pre_checkout_query.answer(ok=True)

async def success(update: Update, context: ContextTypes.DEFAULT_TYPE):
    activate_paid(update.effective_user.id)
    await update.message.reply_text("🔥 Lifetime unlocked")

# ─── POLLING ───────────────────────────────────────────
async def poll(app):
    global last_event_id

    bot = app.bot
    match_id = await get_match()

    while True:
        try:
            if not live_chats:
                await asyncio.sleep(2)
                continue

            data = await fetch_timeline(match_id)
            events = data.get("timeline", [])

            if not events:
                await asyncio.sleep(2)
                continue

            latest = events[-1]
            event_id = latest.get("id")

            if event_id != last_event_id:
                last_event_id = event_id

                player = latest.get("player", {}).get("name")
                runs = latest.get("runs", 0)

                if player:
                    roast = await generate_roast(player, runs)
                    msg = f"🏏 {player} - {runs}\n💀 {roast}"

                    for chat_id in live_chats:
                        await bot.send_message(chat_id=chat_id, text=msg)

        except Exception as e:
            print("ERROR:", e)

        await asyncio.sleep(2)

# ─── MAIN ──────────────────────────────────────────────
def main():
    create_table()

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("live", live))
    app.add_handler(CommandHandler("premium", premium))

    app.add_handler(PreCheckoutQueryHandler(precheckout))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, success))

    async def on_start(app):
        asyncio.create_task(poll(app))

    app.post_init = on_start

    print("🔥 BOT RUNNING")
    app.run_polling()

if __name__ == "__main__":
    main()
