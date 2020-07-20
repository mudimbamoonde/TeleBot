from flask import Flask
import telebot

app = Flask(__name__)
TOKEN = '990949802:AAFemy8K5PSdk5O98flrBpHWupcVW9s5VCU'
bot = telebot.TeleBot(TOKEN)
@app.route("/")
def index():
    return "<h1>Hello</h1>"


if __name__ == "__main__":
    app.run()