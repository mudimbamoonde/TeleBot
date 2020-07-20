#!usr/bin/python3
import telebot
from telebot import types
import time as tm
import requests
import csv
 TOKEN = 'YOUR_TOKEN'


bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()


@bot.message_handler(commands=["start"])
def welcome_message(message):
    # bot.reply_to(message,"Welcome to Zambeef Products PLC")
    bot.send_message(message.chat.id, "Welcome {} to Zambeef Products PLC. \n"
                                      "1. To add complaint add @ and then your complaint.\n"
                                      "2. Search for contact add # then the name of the shop".format(
        message.chat.first_name))
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="News", callback_data="news")
    btn2 = types.InlineKeyboardButton(text="Contacts", callback_data="contact")
    btn3 = types.InlineKeyboardButton(text="Whistle Blower", callback_data="whistleblower")
    btn4 = types.InlineKeyboardButton(text="Retail Outlets", callback_data="retailoutlets")
    about = types.InlineKeyboardButton(text="About Zambeef", callback_data="about")
    markup.add(btn1, btn2, btn3, btn4, about)
    bot.send_message(message.chat.id, "Main Menu", reply_markup=markup)


# lineBot = types.ReplyKeyboardMarkup(row_width=3)
# newsbt = types.KeyboardButton("News")
# ws = types.KeyboardButton("Whistleblower")
# complaint = types.KeyboardButton("Complaints")
# lineBot.add(newsbt,ws,complaint)
# bot.send_message(message.chat.id,"Main Menu",reply_markup=lineBot)


@bot.callback_query_handler(func=lambda call: True)
def BtnReponse(call):
    if call.data == 'menu':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="News", callback_data="news")
        btn2 = types.InlineKeyboardButton(text="Contacts", callback_data="contact")
        btn3 = types.InlineKeyboardButton(text="Whistle Blower", callback_data="whistleblower")
        btn4 = types.InlineKeyboardButton(text="Retail Outlets", callback_data="retailoutlets")
        about = types.InlineKeyboardButton(text="About Zambeef", callback_data="about")
        markup.add(btn1, btn2, btn3, btn4, about)
        # bot.send_message(message.chat.id,"Choose any Icon Below",reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Main Menu",
                              reply_markup=markup)

    elif call.data == 'news':
        newsBTN = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Covid-19 Updates", callback_data="covid19")
        btn2 = types.InlineKeyboardButton(text="About Zambeef", callback_data="companyUpdates")
        btn2 = types.InlineKeyboardButton(text="Other News", callback_data="otherNews")
        btn3 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        newsBTN.add(btn1, btn2, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="News Menu",
                              reply_markup=newsBTN)

    elif call.data == 'contact':
        newsBTN = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Customer Carelines", callback_data="careline")
        btn2 = types.InlineKeyboardButton(text="File Complaint", callback_data="complaints")
        btn3 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        newsBTN.add(btn1, btn2, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Contact Our Careline", reply_markup=newsBTN)


    # Complaints
    elif call.data == "complaints":
        newsBTN = types.InlineKeyboardMarkup(row_width=1)
        btn3 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        newsBTN.add(btn3)
        # bot.reply_to(call.data.message)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="File your Complaint", reply_markup=newsBTN)





    # Contact
    elif call.data == 'careline':
        back = types.InlineKeyboardMarkup(row_width=1)
        btn3 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        back.add(btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Helpdesk Email: \n========================"
                                   "\nzambeef.it@zambeef.co.zm \nHelpdesk Hotlines:"
                                   "\n 211 36 9061 "
                                   "\n 211 36 9060 "
                                   "\n 211 36 9016 "
                                   "\n 211 36 9051"
                                   "\n 0977999015 "
                                   "\n 0966600616 "
                                   "\n 0977999016 "
                                   "\n0978779051", reply_markup=back)




    # Division
    elif call.data == 'allNumbers':

        with open("ShopsLocation.csv", 'rt') as f:
            data = csv.reader(f)
            shopNumbers = 0
            shopName = 0
            for row in data:
                shopName = row[1]
                shopNumbers = row[0]

                bot.send_message(chat_id=call.message.chat.id, text="Shop Name: {}  | Phone Number: {}"
                                                                    "".format(shopName, shopNumbers))
                # break

        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn11 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn11)
        bot.send_message(chat_id=call.message.chat.id, text="Outlets ", reply_markup=outlets)




    # SELECTED
    elif call.data == 'sdp':
        pass

    # Retail Outlets
    elif call.data == 'retailoutlets':
        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Central Province", callback_data="cp")
        btn2 = types.InlineKeyboardButton(text="Copperbelt Province", callback_data="cbp")
    
        btn3 = types.InlineKeyboardButton(text="Southern Province", callback_data="sp")
        btn4 = types.InlineKeyboardButton(text="Northern Province", callback_data="np")
        btn5 = types.InlineKeyboardButton(text="Muchinga Province", callback_data="mp")
        btn6 = types.InlineKeyboardButton(text="North Western Province", callback_data="nwp")
        btn7 = types.InlineKeyboardButton(text="Western Province", callback_data="wp")
        btn8 = types.InlineKeyboardButton(text="Eastern Province", callback_data="ep")
        btn9 = types.InlineKeyboardButton(text="Lusaka Province", callback_data="lp")
        btn10 = types.InlineKeyboardButton(text="Luapula Province", callback_data="lup")
        allNumbers = types.InlineKeyboardButton(text="Check All Number", callback_data="allNumbers")
        btn11 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn1, btn2, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11,allNumbers)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Choose Your Location ", reply_markup=outlets)

        # Retail Outlets
        """Displays Outlets and Area Managers Contacts"""
        # Central Province
    elif call.data == 'cp':
        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Area Managers", callback_data="cpAreaManager")
        ut1 = types.InlineKeyboardButton(text="Outlets", callback_data="outletscp")
        btn2 = types.InlineKeyboardButton(text="Complaints", callback_data="cp")
        back = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn1, btn2, ut1, back)
        bot.send_message(chat_id=call.message.chat.id, text="Central Province ", reply_markup=outlets)

        # Central province AreaManager
    elif call.data == "outletscp":
        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Kapiri Mposhi", callback_data="cp")
        btn2 = types.InlineKeyboardButton(text="Copperbelt Province", callback_data="cbp")
        btn3 = types.InlineKeyboardButton(text="Southern Province", callback_data="sp")
        btn4 = types.InlineKeyboardButton(text="Northern Province", callback_data="np")
        btn5 = types.InlineKeyboardButton(text="Muchinga Province", callback_data="mp")
        btn6 = types.InlineKeyboardButton(text="North Western Province", callback_data="nwp")
        btn7 = types.InlineKeyboardButton(text="Western Province", callback_data="wp")
        btn8 = types.InlineKeyboardButton(text="Eastern Province", callback_data="ep")
        btn9 = types.InlineKeyboardButton(text="Lusaka Province", callback_data="lp")
        btn10 = types.InlineKeyboardButton(text="Luapula Province", callback_data="lup")
        btn11 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn1, btn2, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Choose Your Location ", reply_markup=outlets)

        # Copperbelt Province
    elif call.data == 'cbp':
        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Area Managers", callback_data="cpAreaManager")
        btn2 = types.InlineKeyboardButton(text="Complaints", callback_data="cbp")
        back = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn1, btn2, back)
        bot.send_message(chat_id=call.message.chat.id, text="Copperbelt Province ", reply_markup=outlets)
        # Southern Province
    elif call.data == 'sp':
        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Area Managers", callback_data="cpAreaManager")
        btn2 = types.InlineKeyboardButton(text="Complaints", callback_data="cbp")
        back = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn1, btn2, back)
        bot.send_message(chat_id=call.message.chat.id, text="Southern Province ", reply_markup=outlets)
        # Northern Province
    elif call.data == 'np':
        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Area Managers", callback_data="cpAreaManager")
        btn2 = types.InlineKeyboardButton(text="Complaints", callback_data="cbp")
        back = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn1, btn2, back)
        bot.send_message(chat_id=call.message.chat.id, text="Northern Province ", reply_markup=outlets)
        # Muchinga Province
    elif call.data == 'mp':
        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Area Managers", callback_data="cpAreaManager")
        btn2 = types.InlineKeyboardButton(text="Complaints", callback_data="cbp")
        back = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn1, btn2, back)
        bot.send_message(chat_id=call.message.chat.id, text="Muchinga Province ", reply_markup=outlets)

        # North Western Province
    elif call.data == 'nwp':
        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Area Managers", callback_data="cpAreaManager")
        btn2 = types.InlineKeyboardButton(text="Complaints", callback_data="cbp")
        back = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn1, btn2, back)
        bot.send_message(chat_id=call.message.chat.id, text="North Western Province ", reply_markup=outlets)

    # Western Province
    elif call.data == 'wp':
        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Area Managers", callback_data="cpAreaManager")
        btn2 = types.InlineKeyboardButton(text="Complaints", callback_data="cbp")
        back = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn1, btn2, back)
        bot.send_message(chat_id=call.message.chat.id, text="Western Province ", reply_markup=outlets)

    # Eastern Province
    elif call.data == 'ep':
        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Area Managers", callback_data="cpAreaManager")
        btn2 = types.InlineKeyboardButton(text="Complaints", callback_data="cbp")
        back = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn1, btn2, back)
        bot.send_message(chat_id=call.message.chat.id, text="Eastern Province ", reply_markup=outlets)

        # Lusaka Province
    elif call.data == 'lp':
        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Area Managers", callback_data="cpAreaManager")
        btn2 = types.InlineKeyboardButton(text="Complaints", callback_data="cbp")
        back = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn1, btn2, back)
        bot.send_message(chat_id=call.message.chat.id, text="Lusaka Province ", reply_markup=outlets)

    # Luapula Province
    elif call.data == 'lup':
        outlets = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Area Managers", callback_data="cpAreaManager")
        btn2 = types.InlineKeyboardButton(text="Complaints", callback_data="cbp")
        back = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        outlets.add(btn1, btn2, back)
        bot.send_message(chat_id=call.message.chat.id, text="Luapula Province ", reply_markup=outlets)


    # News
    # companyUpdates
    elif call.data == 'companyUpdates':
        view = types.InlineKeyboardMarkup(row_width=3)
        btn3 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        view.add(btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="https://zambeefplc.com/",
                              reply_markup=view)
    # otherNews
    elif call.data == 'otherNews':
        otherNews = types.InlineKeyboardMarkup(row_width=3)
        btn3 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        otherNews.add(btn3)
        newsSite = "https://www.bbc.com/news"
        bot.send_message(chat_id=call.message.chat.id, text=newsSite)
        bot.send_message(chat_id=call.message.chat.id, text="https://www.znbc.co.zm/news/")
        bot.send_message(chat_id=call.message.chat.id, text="https://www.aljazeera.com/", reply_markup=otherNews)

    # Covid19
    elif call.data == 'covid19':
        view = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton(text="What is Covid-19?", callback_data="whtCovid")
        sympt = types.InlineKeyboardButton(text="Symptoms", callback_data="sympt")
        btn2 = types.InlineKeyboardButton(text="How to prevent", callback_data="prevent")
        statics = types.InlineKeyboardButton(text="Statistics", callback_data="stat")
        treatment = types.InlineKeyboardButton(text="Treatment", callback_data="treatment")
        btn3 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        view.add(btn1, btn2, treatment, sympt, statics, btn3)
        bot.send_message(chat_id=call.message.chat.id, text="Covid-19",
                         reply_markup=view)

    elif call.data == 'whtCovid':
        definition = """Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered 
        coronavirus.Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover 
        without special treatment. """
        whtCovid = types.InlineKeyboardMarkup(row_width=6)
        btn3 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        whtCovid.add(btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=definition, reply_markup=whtCovid)
    # Symptoms
    elif call.data == 'sympt':
        definition = """COVID-19 affects different people in different ways. Most infected people will develop mild 
        to moderate illness and recover without hospitalization. Most common symptoms: fever dry cough tiredness Less 
        common symptoms: aches and pains sore throat diarrhoea conjunctivitis headache loss of taste or smell a rash 
        on skin, or discolouration of fingers or toes Serious symptoms: difficulty breathing or shortness of breath 
        chest pain or pressure loss of speech or movement Seek immediate medical attention if you have serious 
        symptoms. Always call before visiting your doctor or health facility. People with mild symptoms who are 
        otherwise healthy should manage their symptoms at home. On average it takes 5–6 days from when someone is 
        infected with the virus for symptoms to show, however it can take up to 14 days. \n
         https://www.who.int/news-room/q-a-detail/q-a-coronaviruses#:~:text=symptoms"""
        sympt = types.InlineKeyboardMarkup(row_width=6)
        btn3 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        sympt.add(btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=definition, reply_markup=sympt)
    # Prevent
    elif call.data == 'prevent':
        definition = """Protect yourself and others around you by knowing the facts and taking appropriate 
        precautions. Follow advice provided by your local public health agency. To prevent the spread of COVID-19: 
        1.Clean your hands often. \n 2.Use soap and water, or an alcohol-based hand rub. 3.Maintain a safe distance 
        from anyone who is coughing or sneezing.\n 4.Don’t touch your eyes, nose or mouth.\n 5.Cover your nose and 
        mouth with your bent elbow or a tissue when you cough or sneeze.\n 6.Stay home if you feel unwell.\n 7.If you 
        have a fever, cough and difficulty breathing, seek medical attention. Call in advance. Follow the directions 
        of your local health authority. Avoiding unneeded visits to medical facilities allows healthcare systems to 
        operate more effectively, therefore protecting you and others. \n 
        https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public """
        prevent = types.InlineKeyboardMarkup(row_width=6)
        btn3 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        prevent.add(btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=definition, reply_markup=prevent)
    # Statistics
    elif call.data == 'stat':
        re_api = requests.get("https://api.covid19api.com/dayone/country/Zambia")
        # convert to JSON
        results = re_api.json()
        num = len(results)
        # SET PARAMETERS
        confirmedCases = 0
        active = 0
        recovered = 0
        death = 0
        date_c = 0

        for n in range(num):
            confirmedCases = results[n]["Confirmed"]
            active = results[n]["Active"]
            death = results[n]["Deaths"]
            recovered = results[n]["Recovered"]
            date_c = results[n]["Date"]

        stat = "\n Date: {} \n Confirmed Case:{} \n Active Cases: {} \n Recoveries: {} \n Death: {} \n more info " \
               "->https://www.covidvisualizer.com/".format(date_c, confirmedCases, active, recovered, death)
        prevent = types.InlineKeyboardMarkup(row_width=6)
        btn3 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        prevent.add(btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=stat, reply_markup=prevent)

    elif call.data == 'treatment':
        definition = """To date, there are no specific vaccines or medicines for COVID-19. World Health Organization 
        Self care If you feel sick you should rest, drink plenty of fluid, and eat nutritious food. Stay in a 
        separate room from other family members, and use a dedicated bathroom if possible. Clean and disinfect 
        frequently touched surfaces. Everyone should keep a healthy lifestyle at home. Maintain a healthy diet, 
        sleep, stay active, and make social contact with loved ones through the phone or internet. Children need 
        extra love and attention from adults during difficult times. Keep to regular routines and schedules as much 
        as possible. It is normal to feel sad, stressed, or confused during a crisis. Talking to people you trust, 
        such as friends and family, can help. If you feel overwhelmed, talk to a health worker or counsellor.\nMedical 
        treatments If you have mild symptoms and are otherwise healthy, self-isolate and contact your medical 
        provider or a COVID-19 information line for advice. Seek medical care if you have a fever, a cough, 
        and difficulty breathing. Call in advance. """
        prevent = types.InlineKeyboardMarkup(row_width=6)
        btn3 = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        prevent.add(btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=definition, reply_markup=prevent)

        # ABOUT ZAMBEEF PRODUCTS
    elif call.data == 'about':
        about = types.InlineKeyboardMarkup(row_width=1)
        btn = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        about.add(btn)
        # bot.reply_to(chat_id=call.message.chat.text, text="Visit ZAMBEEF PRODUCTS PLC site \n
        # https://zambeefplc.com/")
        bot.send_message(chat_id=call.message.chat.id,
                         text="Visit ZAMBEEF PRODUCTS PLC site \n https://zambeefplc.com/",
                         reply_markup=about)

        # Whistle Blowers
        """ Whistle Blower"""
    elif call.data == 'whistleblower':
        whistle = types.InlineKeyboardMarkup(row_width=1)
        btn = types.InlineKeyboardButton(text="Back to Main Menu", callback_data="menu")
        whistle.add(btn)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Toll Free(9292)\nEmail Us(tipoff@zambeef.co.zm)",
                              reply_markup=whistle)


def find_at(msg):
    for text in msg:
        if '@' in text:
            return text


def find_number(msg):
    for text in msg:
        if '#' in text:
            return text


@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_complaint(message):
    from random import randint
    texts = message.text.split()
    at_text = find_at(texts)
    # bot.reply_to(message, 'https://instagram.com/{}'.format(at_text[1:]))
    bot.reply_to(message, "Thank you for contacting Zambeef Products PLC. Your complaint has been Noted. Your "
                          "Complaint Number is: {}".format(randint(0, 1000)))


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
    # print(at_text)
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="News",callback_data="news")
    btn2 = types.InlineKeyboardButton(text="Contacts", callback_data="contact")
    btn3 = types.InlineKeyboardButton(text="Whistle Blower", callback_data="whistleblower")
    btn4 = types.InlineKeyboardButton(text="Retail Outlets", callback_data="retailoutlets")
    about = types.InlineKeyboardButton(text="About Zambeef", callback_data="about")
    markup.add(btn1, btn2, btn3, btn4, about)
    bot.reply_to(message,text="Main Menu", reply_markup=markup)
    f.close()



#
# bot.polling()
while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        tm.sleep(1)
