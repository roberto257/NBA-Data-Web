#Import dependencies
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd

import requests

import json
from scrape import *

from flask import Flask, render_template, jsonify, request, escape, url_for

data = scrape_data()
headers = data_headers()

app = Flask(__name__)

#Get out list to post

nba = scrape_data()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_get_data', methods = ['POST'])
def _get_data():
    return jsonify({'data' : data})

if __name__ == "__main__":
    app.run(debug = True)

