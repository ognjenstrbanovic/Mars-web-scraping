# import necessary libraries
from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)
# Create connection variable
connection = 'mongodb://localhost:27017/mars_app'
# Pass connection to the pymongo instance.
client = pymongo.MongoClient(connection)
# Connect to a database. Will create one if not already available.
db = client.mars
# Drops collection if available to remove duplicates
db.mars.drop()
# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri=connection)

# create route that renders index.html template
@app.route("/")
def index():
    scraped_data = mongo.db.scraped_data.find_one()
    return render_template("index.html", scraped_data = scraped_data)

@app.route("/scrape")
def scraper():
    scrapes = mongo.db.scraped_data
    scrapes.update({}, scrape_mars.scrape(), upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)