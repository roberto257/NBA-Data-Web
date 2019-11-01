#Import dependencies
from flask import Flask, render_template, request
#Import our scraping script
import scrape 

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    return scrape.scrape_data()
   
if __name__ == "__main__":
    app.run(debug = True)
