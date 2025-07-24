from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN: Final= "7629948369:AAHG3avP7AQ_NfD6_jUvJwmRnlnLAnuBLiA"

BOT_USERNAME: Final = "@wadia1_bot"


#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me!! I am Wadia")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am Wadia. Type something to chat with me!!")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custome command!")


# reasponses
def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'hi there'
    
    if 'how are you' in processed:
        return 'I am fine'
    
    if 'what is your name' in processed:
        return 'I am Wadia'
    
    if 'what is your age' in processed:
        return 'I am a bot'
    
    if 'where are you from' in processed:
        return 'I am from Bangladesh'
    
    return "I don't know what you are talking about"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: {text}")

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
            #await update.message.reply_text(response)
        else:
            return
    else:
        response = handle_response(text)

    print(f"Bot: {response}")
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == '__main__':
    print("starting bot...")
    app =  ApplicationBuilder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # errors
    app.add_error_handler(error)

    #pulls the bot
    print("polling bot...")
    app.run_polling(poll_interval=3)