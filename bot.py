import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Command handler function
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello!')

def main() -> None:
    # Get the Telegram bot token from the environment variable
    token = os.getenv('TELEGRAM_API_TOKEN')  # Set this variable in your environment or Railway settings
    if not token:
        print("Error: Telegram API token is missing!")
        return
    
    # Create the Application and set up the handlers
    application = Application.builder().token(token).build()

    # Add /start command handler
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
