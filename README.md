# chatbot-
Project Overview
This project is a simple chatbot application built using Flask for the backend and HTML/JavaScript for the frontend. The chatbot can answer predefined questions from a corpus and maintains conversation history for a more interactive user experience.

Prerequisites
Python 3.x
pip (Python package installer)
Installation and Setup
Clone the Repository

git clone https://github.com/your-repo/chatbot.git
cd chatbot
Install Dependencies

Install Flask and NLTK:
pip install flask
pip install nltk
Download NLTK Data

Create a Python script named download_nltk_data.py with the following content:

python

import nltk
nltk.download('punkt')
Run the script to download the required NLTK data:

python download_nltk_data.py
Set Up Corpus File

Make sure you have a corpus.json file in your project directory. It should contain the question-answer pairs for the chatbot. An example corpus.json file is provided in the project.

Run the Flask Application

Start the Flask server by running:

python app.py
Access the Chatbot

Open your web browser and navigate to http://127.0.0.1:5000 to interact with the chatbot.

Folder Structure
app.py: The main Python script running the Flask application.
corpus.json: JSON file containing the chatbot's question-answer corpus.
templates/index.html: HTML file for the chatbot's frontend.
Troubleshooting
KeyError: Ensure the conversation key is always included in the JSON data sent to the backend. The backend should handle the absence of this key gracefully.
NLTK Data Download Issues: Ensure you have an active internet connection when running download_nltk_data.py

#IMPORTANT index.html file inside the templates folder  and all file like app.py , corpus.json,templates in one folder .

