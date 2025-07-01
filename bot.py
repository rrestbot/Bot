from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8067847794:AAFk8_714M9CohQ6Dz-V4lYstloWTXL6hgE"
CHANNEL_ID = -1002831436891

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("বট শুরু হয়েছে! যেকোনো মেসেজ দিলে আমি চ্যানেলে পাঠাবো।")

async def forward_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=update.message.text)
        await update.message.reply_text("✅ তোমার মেসেজ চ্যানেলে পাঠানো হয়েছে!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_channel))

print("Bot is running...")
app.run_polling()
