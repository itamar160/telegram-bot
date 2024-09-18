import hashlib
import telebot
import os

FILE_NAME = "telegramPhoto.jpg"
f = open(FILE_NAME, "w+")
f.close()


def hash_image():
    with open(FILE_NAME, "rb") as f:
        hash_val = hashlib.sha256(f.read()).hexdigest()
    f.close()
    return hash_val


API_KEY = '6845798336:AAH0MFJEUKVIBwrjGlEUXi5n3GwhhOSMf8w'
bot = telebot.TeleBot(API_KEY)


@bot.message_handler()
def handle_text(message):
    bot.send_message(message.chat.id, "error: send an image not text")


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_path = bot.get_file(message.photo[-1].file_id).file_path

    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".jpg" or ext == ".jpeg":
        hash_from_file_path(message, file_path)
    else:
        bot.send_message(message.chat.id, "error: file is not an image")


@bot.message_handler(func=lambda message: True,
                     content_types=['audio', 'voice', 'video', 'text', 'location', 'contact', 'sticker'])
def handle_other(message):
    bot.send_message(message.chat.id, "error: file is not an image")


@bot.message_handler(content_types=['document'])
def handle_document(message):
    print("1")
    file_path = bot.get_file(message.document.file_id).file_path

    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".jpg" or ext == ".jpeg":
        hash_from_file_path(message, file_path)
    else:
        bot.reply_to(message, "error: file is not an image")


def hash_from_file_path(message, file_path):
    file = bot.download_file(file_path)

    with open(FILE_NAME, "wb") as code:
        code.write(file)
    code.close()

    val = hash_image()

    bot.reply_to(message, "hash value: {}".format(val))


bot.polling()