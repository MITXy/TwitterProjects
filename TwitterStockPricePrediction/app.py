from flask import Flask, request, jsonify
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import joblib
import numpy as np

app = Flask(__name__)

# Load pre-built model
model = joblib.load('Stock_price_model.joblib')

# Perform sentiment analysis on input tweets
nltk.download('vader_lexicon')
SS = SentimentIntensityAnalyzer()


@app.route('/')
def home():
    return 'Hello, I predict price stocks by analysing Sentiments from Tweets!'


@app.route('/predict', methods=['GET'])
def predict():
    tweets = request.args.get('tweets')
    sentiment_scores = round(SS.polarity_scores(tweets)['compound'], 2)
    trans_data = pd.DataFrame({'sentiment_score': sentiment_scores}, index=[0]).values
    y = np.round(model.predict(trans_data), 2)
    return jsonify({'predictions': list(y)})


if __name__ == '__main__':
    app.run(debug=True)
