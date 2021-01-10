import telebot
from ImageProcessing import *
import os

TOKEN = '1484122424:AAGgsvY7sh9RrLiRUFcvoGmtMIoBsm3t0Rg'

bot = telebot.TeleBot(TOKEN)
bot_alias = '@' + bot.get_me().username

@bot.message_handler(commands=['start'])
def startPrivet(message):
    texts = "Здраствуй, это бот который может обработать фотографию.\nПришлите фотографию документом!"
    bot.send_message(chat_id=message.chat.id, text=texts)


@bot.message_handler(content_types=['document'])
def handle(message):
    save_dir = os.getcwd()
    file_name = message.document.file_name
    file_id = message.document.file_name
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    file_name = message.from_user.username + file_name
    print(file_name)
    with open(save_file + "/"+ file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Ещё немного...')
    url = image_processing(file_name)
    with open(url, 'rb') as doc:
        bot.send_document(message.chat.id, doc)
        


bot.polling()
