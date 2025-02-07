import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Command handler function
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello!')

async def main() -> None:
    # Telegram API token ko environment se laana
    token = os.getenv('TELEGRAM_API_TOKEN')  # Isko apne environment ya Railway settings mein set karein
    if not token:
        print("Error: Telegram API token missing hai!")
        return
    
    # Application ko create karna aur handlers set karna
    application = Application.builder().token(token).build()

    # /start command handler add karna
    application.add_handler(CommandHandler("start", start))

    # Bot ko start karna
    await application.run_polling()

# Agar aap Railway pe deploy kar rahe hain, to yeh line hata dijiye
# asyncio.run(main()) ko is tarah replace karein
if __name__ == '__main__':
    import asyncio
    # Railway ya aise environment mein jo already event loop chala rahe hain
    asyncio.get_event_loop().run_until_complete(main())
