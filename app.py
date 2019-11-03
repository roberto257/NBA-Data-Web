
#Import our external web scraping file
from scrape import *

#Flask dependencies
from flask import Flask, render_template, jsonify, request, escape, url_for

#Get our lists to post
headers = data_headers()

#Start the flask app
app = Flask(__name__)

#Start page
@app.route('/')
def index():
    return render_template('index.html')

#What happens when our button is clicked
@app.route('/_get_data')
def _get_data():
    #Get the name we want to search for
    searchName = request.args.get('searchName')
    #Call the function and pass our search name parameter
    dataList = scrape_data(searchName)

    #Return the json format of the data we scraped
    return jsonify(dataList = dataList)

#Run the app
if __name__ == "__main__":
    app.run(debug = True)
