import asyncio
from telegram.ext import ApplicationBuilder, MessageHandler, filters

TOKEN = "PASTE_YOUR_TOKEN_HERE"

async def handle(update, context):
    query = update.message.text
    
    msg = await update.message.reply_text(
        f"Searching {query}..."
    )
    
    await asyncio.sleep(2)
    
    sent = await update.message.reply_text(
        "Episode found (demo)"
    )
    
    await asyncio.sleep(1200)
    
    await sent.delete()

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()
