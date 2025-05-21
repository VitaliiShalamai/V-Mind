
import os
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

def handle_message(update, context):
    user_input = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ты — Край. Ассистент Виталия. Отвечаешь по делу, жёстко, без воды, с характером."},
            {"role": "user", "content": user_input}
        ]
    )
    text_response = response['choices'][0]['message']['content']
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_response)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет. Это Край. Пиши.")

def main():
    print("Край в сети")
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    