import requests
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return requests.get('https://www.google.com/').text
