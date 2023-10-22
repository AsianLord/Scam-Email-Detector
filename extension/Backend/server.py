from flask import Flask, json, jsonify, request
from flask_cors import CORS, cross_origin

import pandas as pd
import numpy as np
from textblob import TextBlob 
import nltk
import string
from sklearn import tree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods = ['POST'])
@cross_origin()
def email_request():
	print(request.form["email"])

app.run(port=5000)



"""
Machine Learning
"""
model_filename = "email_scam_detection_model.sav"
vectorizer_filename = "email_scam_vectorizer.pkl"

def preprocess_email(email):
    # Convert the email into lower case and remove all of the punctuation
    email = str(email).lower()
    no_punc_email = email.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))

    # Convert this email text into a TextBlob to prepare for further processing
    tb_email = TextBlob(no_punc_email)

    # Tokenise the email into its words and remove all of the stopwords
    email_words = tb_email.words
    stopword_free_list = [word for word in email_words if word not in stopwords.words("english")]

    # Stem each word of the email word list and join the list into a full string
    stemmed_words = []
    for word in stopword_free_list:
        stemmed_words.append(word.stem())
    stemmed_words = " ".join(stemmed_words)

    # Finally load the TfidfVectorizer so we can transform the processed email into a format for the model to predict on
    vectorizer = pickle.load(open(vectorizer_filename, "rb"))
    return vectorizer.transform([stemmed_words]).toarray()

def predict(email):
    # Process the email into the correct format
    processed_email = preprocess_email(email)

    # Load the fraud email detection model and predict whether the email is fraudulent or not
    fraud_email_model = pickle.load(open(model_filename, "rb"))
    return fraud_email_model.predict(processed_email)[0]

def process_email_request(email):
    email = preprocess_email(email)
    return predict(email)
