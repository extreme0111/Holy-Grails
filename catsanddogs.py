from telegram.ext import Updater, CommandHandler
from telegram import Bot
import asyncio
my_queue = asyncio.Queue()
import requests  # HTTP library for Python
import re   # regular expression, more practise on this next time

def get_correct_image_url(suffix):
    extensions = ['jpg', 'png', 'jpeg']
    if suffix in extensions:
        return True
    else:
        return False

def get_image_url(amimal):
    if amimal == 'dog':
        contents = requests.get('https://random.dog/woof.json').json()
        print(contents, 'url received')
        url = contents['url']
        file_extension = re.search("([^.]*)$",url).group(1).lower()
        while get_correct_image_url(file_extension) == False:
            contents = requests.get('https://random.dog/woof.json').json()
            url = contents['url']
            file_extension = re.search("([^.]*)$",url).group(1).lower()
            print(file_extension, contents)
        return url
    elif amimal == 'cat':
        contents = requests.get('https://api.thecatapi.com/v1/images/search').json()
        url = contents[0]['url']
        file_extension = re.search("([^.]*)$",url).group(1).lower()
        while get_correct_image_url(file_extension) == False:
            contents = requests.get('https://api.thecatapi.com/v1/images/search').json()
            url = contents[0]['url']
            file_extension = re.search("([^.]*)$",url).group(1).lower()
        return url

YOUR_TOKEN = "7131095261:AAEmRfzNbP0GwQfkrKhivUi516O1zQrh7oU" #Add your bot token here
bot = Bot(YOUR_TOKEN)

def doggo(update, context):
    url = get_image_url('dog')
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def catto(update, context):
    url = get_image_url('cat')
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater(YOUR_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('doggo', doggo))
    dp.add_handler(CommandHandler('catto', catto))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

