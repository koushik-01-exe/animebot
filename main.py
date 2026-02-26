import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    await update.message.reply_text(f"Searching: {text}")
    
    await asyncio.sleep(2)
    
    sent = await update.message.reply_text("Anime found (demo)")
    
    await asyncio.sleep(1200)
    
    await sent.delete()

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()
