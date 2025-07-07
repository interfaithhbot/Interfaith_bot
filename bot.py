import telebot
import os

TOKEN = os.getenv("8015234858:AAG5rcxadMUVL60_XDsIigGngcdvcMlzS34")
bot = telebot.TeleBot(TOKEN)

response_text = """@friendship_chattingbot
@friendship_chattingbot
@friendship_chattingbot

𝐬𝐭𝐞𝐩𝟏: 𝐬𝐭𝐚𝐫𝐭 𝐛𝐨𝐭 
𝐬𝐭𝐞𝐩𝟐: 𝐭𝐚𝐤𝐞 𝐬𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭 𝐚𝐧𝐝 
            𝐬𝐞𝐧𝐝 𝐭𝐨 @vedio_seller
𝐬𝐭𝐞𝐩𝟒: 𝐠𝐞𝐭 𝐟𝐫𝐞𝐞 𝐯𝐢𝐝𝐞𝐨 𝐠𝐫𝐨𝐮𝐩
"""

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, response_text)

@bot.message_handler(func=lambda msg: msg.text and msg.text.lower() == "hi")
def handle_hi(message):
    bot.send_message(message.chat.id, response_text)

bot.infinity_polling()
