from flask import Flask, request
from flask import jsonify
import json
import markdown.extensions.fenced_code
import tools.getdata as get
import tools.postdata as pos




app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown( 
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template

@app.route("/authors")
def authors_():
    quotes = get.authors()
    return jsonify(quotes)

@app.route("/tags")
def tags_():
    quotes = get.tags()
    return jsonify(quotes)

@app.route("/quotes")
def quotes_():
    quotes = get.quotes()
    return jsonify(quotes)

@app.route("/quotes/<author>")
def quotes_author_(author):
    quotes = get.quotes_author(author)
    return jsonify(quotes)

@app.route("/quotes_tag/<tag>")
def quotes_tag_(tag):
    quotes = get.quotes_tag(tag)
    return jsonify(quotes)

@app.route("/quotes_sentiment_gte/<sentiment_compound>")
def quotes_sentiment_gt_(sentiment_compound):
    quotes = get.quotes_sentiment_gte(sentiment_compound)
    return jsonify(quotes)

@app.route("/quotes_sentiment_lte/<sentiment_compound>")
def quotes_sentiment_lt_(sentiment_compound):
    quotes = get.quotes_sentiment_lte(sentiment_compound)
    return jsonify(quotes)



@app.route("/newquote", methods=["POST"])
def insert_quote_():
    quote = request.form.get("quote")
    author = request.form.get("author")
    tag1 = request.form.get("tag1")
    tag2 = request.form.get("tag2")
    tag3 = request.form.get("tag3")
    tag4 = request.form.get("tag4")
    tag5 = request.form.get("tag5")
    tag6 = request.form.get("tag6")
    pos.insert_quote(quote, author, tag1, tag2, tag3, tag4, tag5, tag6)
    return "Se ha introducido la quote en la base de datos"



app.run("0.0.0.0", 5000, debug=True)