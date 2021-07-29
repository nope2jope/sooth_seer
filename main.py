from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

@app.route('/', methods=['GET','POST'])
def home():
    cards = 0
    clicked = False
    return render_template("index.html", c=cards, bool=clicked)

@app.route('/one-card')
def one_card():
    cards = 1
    clicked = True
    return render_template("index.html", c=cards, bool=clicked)

if __name__ == "__main__":
    app.run(debug=True, port=8000)