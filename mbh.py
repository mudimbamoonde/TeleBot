#!usr/bin/python3
import telebot
from telebot import types
import time as tm
import requests
import csv

# TOKEN = '1232927523:AAF_2sTtpiVE817pXvwcVzV34FkfxHwGARI'
# TOKEN = '1090878731:AAGbXJuQF5lwiAnlcQX1k3dYQkaUS5jldg8'
TOKEN = '990949802:AAFemy8K5PSdk5O98flrBpHWupcVW9s5VCU'  # MBH

bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()


@bot.message_handler(commands=["start"])
def welcome_message(message):
    # bot.reply_to(message,"Welcome to Zambeef Products PLC")
    bot.send_message(message.chat.id, "Welcome {} to Mudimba Health Care. \n"
                                      "1. To add complaint add @ and then your complaint.\n"
                                      "2. Search for contact add # then the name of the shop".format(
        message.chat.first_name))
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="News", callback_data="news")
    btn2 = types.InlineKeyboardButton(text="Contacts", callback_data="contact")
    btn3 = types.InlineKeyboardButton(text="Whistle Blower", callback_data="whistleblower")
    btn4 = types.InlineKeyboardButton(text="Retail Outlets", callback_data="retailoutlets")
    about = types.InlineKeyboardButton(text="About MBHC", callback_data="about")
    markup.add(btn1, btn2, btn3, btn4, about)
    bot.send_message(message.chat.id, "Main Menu", reply_markup=markup)


# lineBot = types.ReplyKeyboardMarkup(row_width=3)
# newsbt = types.KeyboardButton("News")
# ws = types.KeyboardButton("Whistleblower")
# complaint = types.KeyboardButton("Complaints")
# lineBot.add(newsbt,ws,complaint)
# bot.send_message(message.chat.id,"Main Menu",reply_markup=lineBot)


def find_number(msg):
    for text in msg:
        if '#' in text:
            return text

def findNumber(name):
    with open("ShopsLocation.csv", 'r') as f:
        data = csv.reader(f)
        for row in data:
            # shop = row[0] + " => " + row[1]
            if name in row[1]:
                return row[0] + " => " + row[1]
            else:
                return "No Shop by the name: {}".format(name)
        
            


@bot.message_handler(func=lambda msg: msg.text is not None and '#' in msg.text)
def at_number(message):
    from random import randint
    texts = message.text.split()
    at_text = find_number(texts)
    finer = message.text
    search = finer.replace('#', "")
    with open("shop.csv", 'r') as f:
        data = csv.reader(f)
        out = []
        for row in data:
            # shop = row[0] + " => " + row[1]
            if search in row[1]:
                res = row[0] + " => " + row[1]
                bot.reply_to(message,text=res )

            # else:
            #     out = "No Shop by the name: {}".format(search)
            #     bot.reply_to(message,text=out)
    f.close()
    # print(at_text)
  
bot.polling()
# while True:
#     try:
#         bot.polling(none_stop=True)
#     except Exception:
#         tm.sleep(1)
