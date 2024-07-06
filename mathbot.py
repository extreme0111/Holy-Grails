from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Bot, BotCommand
import asyncio
my_queue = asyncio.Queue()
import requests  # HTTP library for Python
import re   # regular expression, more practise on this next time
import random

YOUR_TOKEN = "7359002071:AAEq7wJ0w-ftmhLdSA52PFncckCOMQjoZDM" #Add your bot token here
bot = Bot(YOUR_TOKEN)
answer = 0
botstate = ''


def handler(update, context):
    global botstate
    message = update.message['text']
    if botstate == 'addasking':
        addition(update, context, int(message))
    elif botstate == 'addanswering':
        answering(update, context, answer, message)

    if botstate == 'minusasking':
        subtraction(update, context, int(message))
    elif botstate == 'minusanswering':
        answering(update, context, answer, message)

    if botstate == 'multiasking':
        multiplication(update, context, int(message))
    elif botstate == 'multianswering':
        answering(update, context, answer, message)

    if botstate == 'overasking':
        division(update, context, int(message))
    elif botstate == 'overanswering':
        answering(update, context, answer, message)
        
def addasker(update, context):
    update.message.reply_text('How many numbers would you like in the equation?')
    global botstate
    botstate = 'addasking'

def minusasker(update, context):
    update.message.reply_text('How many numbers would you like in the equation?')
    global botstate
    botstate = 'minusasking'

def multiasker(update, context):
    update.message.reply_text('How many numbers would you like in the equation?')
    global botstate
    botstate = 'multiasking'

def overasker(update, context):
    update.message.reply_text('How many numbers would you like in the equation?')
    global botstate
    botstate = 'overasking'

def addition(update, context, number):
    nums = []
    equation = ''
    randnum = 0
    for i in range(number):
        randnum = random.randint(1, 100)
        nums.append(randnum)
        equation += str(randnum) + ' + '
    equation = equation[0:-3]
    global botstate
    botstate = 'addanswering'
    update.message.reply_text(equation)
    global answer
    answer = 0
    for i in nums:
        answer += i

def subtraction(update, context, number):
    nums = []
    equation = ''
    randnum = 0
    for i in range(number):
        randnum = random.randint(1, 100)
        nums.append(randnum)
        equation += str(randnum) + ' - '
    equation = equation[0:-3]
    global botstate
    botstate = 'minusanswering'
    update.message.reply_text(equation)
    global answer
    answer = nums[0]
    for i in range(1, len(nums)):
        answer -= nums[i]
        

def multiplication(update, context, number):
    nums = []
    equation = ''
    randnum = 0
    for i in range(number):
        randnum = random.randint(1, 10)
        nums.append(randnum)
        equation += str(randnum) + ' × '
    equation = equation[0:-3]
    global botstate
    botstate = 'multianswering'
    update.message.reply_text(equation)
    global answer
    answer = 1
    for i in nums:
        answer *= i

def division(update, context, number):
    equation = ''
    x = random.randint(1,10)
    randnum = x
    for i in range(number):
        y = random.randint(1, 10)
        randnum = randnum * y
        equation = equation + ' ÷ ' + str(y)
        print(equation)
    equation = str(randnum) + equation
    print(equation)
    update.message.reply_text(equation)
    global botstate
    botstate = 'overanswering'
    global answer
    answer = x

def answering(update, context, answer, message):
    if message == str(answer):
        update.message.reply_text('Correct!')
    else:
        update.message.reply_text('Wrong answer, try again. ' + 'Correct answer was ' + str(answer) + '.')

def main():
    updater = Updater(YOUR_TOKEN)
    command = [BotCommand("addition","Try an addition question"), BotCommand("subtraction", "Try a subtraction question"), BotCommand("multiplication","Try a multiplication question"), BotCommand("division", "Try a division question")]
    bot.set_my_commands(command)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('addition', addasker))
    dp.add_handler(CommandHandler('subtraction', minusasker))
    dp.add_handler(CommandHandler('multiplication', multiasker))
    dp.add_handler(CommandHandler('division', overasker))
    dp.add_handler(MessageHandler(Filters.text, handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()