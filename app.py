from flask import Flask, jsonify, redirect, render_template
import pymongo
import scrape_mars


client = pymongo.MongoClient('mongodb://localhost:27017/')


app = Flask(__name__)


db = client.mars_data_DB
mars_collection = db.mars_collection

@app.route("/")
def render_index():


@app.route('/scrape')
def scrape_mars_data():
    scrape_results = scrape_mars.scrape()
    mars_collection.replace_one({}, scrape_results, upsert=True)
    return redirect('http://localhost:5000/', code=302)

if __name__ == '__main__':
    app.run()