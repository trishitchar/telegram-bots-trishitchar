from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

token = "Replace with your token id"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! Welcome to the Trishitchar bot. /help - to Display available commands")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_message = """
    Available commands:
    /start - Welcome message
    /help - Display available commands
    /social - Social media link
    /contact - Contact information
    """
    await update.message.reply_text(help_message)

async def social(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Insta : instagram.com/trishit.char")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Twitter : twitter.com/trishitchar")

app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("social", social))
app.add_handler(CommandHandler("contact", contact))

app.run_polling()
