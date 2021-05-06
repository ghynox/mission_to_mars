#import dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping2

#define app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#define the route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#add the scrape page
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping2.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

#run the code
if __name__ == "__main__":
    app.run()