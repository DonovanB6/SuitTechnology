import os
from urllib.request import urlretrieve as retrieve
from werkzeug.utils import secure_filename

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from config import flow

from flask import Flask, render_template, request, redirect, flash, url_for

bot = ChatBot("SuitBot")
trainer = ListTrainer(bot)
trainer.train(flow)


app = Flask(__name__)


# Function to display our home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/get")
def get_bot_response():
    user_response = request.args.get('msg')
    return str(bot.get_response(user_response))


app.secret_key = 'some_secret_key'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)