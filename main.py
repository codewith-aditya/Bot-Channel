from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os
import asyncio

# Get the token from environment variables (for security)
TOKEN = os.getenv("BOT_TOKEN")

# List of usernames to send the messages
usernames = ['Tech_Shreyansh29', 'abhirai23']

# Function to send messages
async def forward_message(update: Update, context):
    message_text = update.message.text
    for username in usernames:
        try:
            await context.bot.send_message(chat_id=f'@{username}', text=message_text)
        except Exception as e:
            print(f"Failed to send message to {username}: {e}")

# Start command
async def start(update: Update, context):
    await update.message.reply_text('Bot is up and running!')

# Main function
async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    print("Bot is starting...")
    await application.run_polling()

# Run the bot
if __name__ == '__main__':
    asyncio.run(main())
