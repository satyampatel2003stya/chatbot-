from flask import Flask, request, jsonify, render_template
import nltk
from nltk.tokenize import word_tokenize
import json
import os

app = Flask(__name__)

# Specify the path to the corpus.json file
corpus_path = os.path.join(os.path.dirname(__file__), 'corpus.json')

# Load the corpus
with open(corpus_path, 'r') as f:
    corpus = json.load(f)

def answer_from_corpus(question):
    tokens = word_tokenize(question.lower())
    for item in corpus:
        if all(token in item['question'].lower() for token in tokens):
            return item['answer']
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    conversation = data.get('conversation', [])

    answer = answer_from_corpus(question)
    if not answer:
        answer = 'invalid question try again.'

    # Update the conversation history
    conversation.append({"sender": "user", "message": question})
    conversation.append({"sender": "bot", "message": answer})

    return jsonify({'answer': answer, 'conversation': conversation})

if __name__ == '__main__':
    app.run(debug=True)
