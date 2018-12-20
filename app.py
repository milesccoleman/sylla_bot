from flask import Flask, render_template, request
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

app = Flask(__name__)

bot = ChatBot('LBH_BOT',
    filters=["chatterbot.filters.RepetitiveResponseFilter"], 
    read_only=False,
)             

conv = open('chats.txt', 'r').readlines()

bot.set_trainer(ListTrainer)

bot.train(conv)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()
