from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

@app.route('/')
def home():
    cards = [0, 1, 3]
    return render_template("index.html", c=cards)



if __name__ == "__main__":
    app.run(debug=True, port=8000)