from sooth_sayer import croupier, deck_writer
from pprint import pprint
import os.path
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# checks to see if csv exists
# if not, runs functions to scrape and format card info
if not os.path.exists('tarot_deck.csv'):
    deck_writer.write_deck()

# retrieves info from csv file
tarot_deck = deck_writer.fetch_deck()

@app.route('/', methods=['GET','POST'])
def home():
    cards = 0
    clicked = False
    return render_template("index.html", c=cards, bool=clicked)

@app.route('/one-card')
def one_card():
    fortune = croupier.fortune_teller(deck=tarot_deck, spread=1)
    cards = 1
    clicked = True
    return render_template("index.html", c=cards, f=fortune, bool=clicked)

@app.route('/three-card')
def three_card():
    fortune = croupier.fortune_teller(deck=tarot_deck, spread=3)
    cards = 3
    clicked = True
    pprint(fortune[0])
    return render_template("index.html", c=cards, f=fortune, bool=clicked)

@app.route('/four-card')
def four_card():
    fortune = croupier.fortune_teller(deck=tarot_deck, spread=4)
    cards = 4
    clicked = True
    return render_template("index.html", c=cards, f=fortune, bool=clicked)

if __name__ == "__main__":
    app.run(debug=True, port=8000)