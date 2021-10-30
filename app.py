# import json
# import random
from config import flow

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.preprocessing import LabelEncoder
# import numpy as np
# from tensorflow.keras.models import load_model
import json
# import random

# importing training data
# training_data = pd.read_csv("training_data2.csv")
# # loading model
# chatbot = load_model('chatbot')
# # loading responses
# responses = json.load(open("responses.json", "r"))
#
# training_data["patterns"] = training_data["patterns"].str.lower()
# vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
# vectorizer.fit(training_data["patterns"])
#
# le = LabelEncoder()
# le.fit(training_data["tags"])


intents = json.loads(open("responses.json").read())
bot = ChatBot("suitbot")
trainer = ListTrainer(bot)
trainer.train(str(flow))
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

app = Flask(__name__)


# def predict_tag(inp_str):
#     inp_data_tfidf = vectorizer.transform([inp_str.lower()]).toarray()
#     predicted_proba = chatbot.predict(inp_data_tfidf)
#     encoded_label = [np.argmax(predicted_proba)]
#     predicted_tag = le.inverse_transform(encoded_label)[0]
#     return predicted_tag


# Function to display our home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    # tag = predict_tag(userText)
    # response = random.choice(responses[tag])
    # return response
    return str(bot.get_response(userText))


# def start_chat():
#     while True:
#         if userText == "EXIT":
#             break
#         else:
#             if inp:
#                 tag = predict_tag(inp)
#                 response = random.choice(responses[tag])
#                 print("Response... : ", response)
#             else:
#                 pass

#     msg = request.form["msg"]
#     if msg.startswith('my name is'):  # handles users name
#         name = msg[11:]  # get name
#         ints = predict_class(msg, model)  # get class of responses
#         res1 = getResponse(ints, intents)  # get actual response
#         res = res1.replace("{n}", name)  # insert name and response
#     elif msg.startswith('hi my name is'):
#         name = msg[14:]
#         ints = predict_class(msg, model)
#         res1 = getResponse(ints, intents)
#         res = res1.replace("{n}", name)
#     else:
#         ints = predict_class(msg, model)
#         res = getResponse(ints, intents)
#     return res
#
#
# def predict_class(sentence, model):
#     # filter out predictions below a threshold
#     p = bow(sentence, words, show_details=False)
#     res = model.predict(np.array([p]))[0]
#     ERROR_THRESHOLD = 0.25
#     results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
#     # sort by strength of probability
#     results.sort(key=lambda x: x[1], reverse=True)
#     return_list = []
#     for r in results:
#         return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
#     return return_list

# def getResponse(ints, intents_json):
#     tag = ints[0]["intent"]
#     list_of_intents = intents_json["intents"]
#     for i in list_of_intents:
#         if i["tag"] == tag:
#             result = random.choice(i["responses"])
#             break
#     return result


@app.route('/about')
def about_us():
    return render_template('about.html')


app.secret_key = 'some_secret_key'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
