import spacy

from config import flow

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


bot = ChatBot("suitbot")
trainer = ListTrainer(bot)
trainer.train(str(flow))
trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.english")


app = Flask(__name__)


# Function to display our home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


app.secret_key = 'some_secret_key'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)