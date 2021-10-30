import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import save_model

training_data = pd.read_csv("training_data2.csv")

training_data["patterns"] = training_data["patterns"].str.lower()
vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
training_data_tfidf = vectorizer.fit_transform(training_data["patterns"]).toarray()

le = LabelEncoder()
training_data_tags_le = pd.DataFrame({"tags": le.fit_transform(training_data["tags"])})
training_data_tags_dummy_encoded = pd.get_dummies(training_data_tags_le["tags"]).to_numpy()

chatbot = Sequential()
chatbot.add(Dense(10, input_shape=(len(training_data_tfidf[0]),)))
chatbot.add(Dense(8))
chatbot.add(Dense(8))
chatbot.add(Dense(6))
chatbot.add(Dense(len(training_data_tags_dummy_encoded[0]), activation="softmax"))
chatbot.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])

chatbot.fit(training_data_tfidf, training_data_tags_dummy_encoded, epochs=50, batch_size=42)

save_model(chatbot, "chatbot")
