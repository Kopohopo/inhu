from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.error import Unauthorized

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '7166081939:AAFC3rRR4_AwNHiRMc0sglXLrM1b5lwx7BU'

# List of admin chat IDs
ADMIN_CHAT_IDS = []

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot is running!')

def check_message(update: Update, context: CallbackContext) -> None:
    # Check if the message has been edited
    if update.edited_message:
        # Get the edited message
        edited_message = update.edited_message
        # Report the edited message to all admins
        for admin_chat_id in ADMIN_CHAT_IDS:
            try:
                context.bot.send_message(chat_id=admin_chat_id, text=f"Message edited in group {update.message.chat_id} by user {edited_message.from_user.username}:\n{edited_message.text}")
            except Unauthorized:
                print(f"Unauthorized: Could not send message to admin {admin_chat_id}")
        # Delete the edited message
        edited_message.delete()

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.all & (~Filters.command), check_message))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
