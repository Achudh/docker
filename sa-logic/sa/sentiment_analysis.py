from textblob import TextBlob
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/analyse/sentiment", methods=['GET', 'POST'])
def analyse_sentiment():
    sentence = request.get_json()['sentence']
    polarity = TextBlob(sentence).sentences[0].polarity
    return jsonify(
        sentence=sentence,
        polarity=polarity
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#docker run -d -p 8080:8080 -e SA_LOGIC_API_URL='http://0.0.0.0:5000' achudh/sentiment-analysis-web-app