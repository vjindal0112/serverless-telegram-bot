import telegram
import sys
import os
TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = '-488207708'
def send_message(event, context):
    bot = telegram.Bot(token=TOKEN)
    bot.sendMessage(chat_id = CHAT_ID, text = 'Hey Enlight, do your standups, post in maker log, and update the metrics sheet')
