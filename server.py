from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://bobbert:CqWe4rBnQ6uBKua@cluster0.ar6xvsm.mongodb.net/test')
db = client['test']
tweets_col = db['tweets']

@app.route('/')
def index():
    return render_template('show_data.html')

@app.route('/get_tweets', methods=['POST'])
def get_():
    tweets = list(tweets_col.find())

    for tweet in tweets:
        tweet['_id'] = str(tweet['_id'])

    return jsonify(tweets)

if __name__ == '__main__':
    app.run(debug=True)
