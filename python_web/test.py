import json

from flask import Flask, render_template


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'my_very_very_secret_key'




@app.route("/")
def passiv():
    user = 'Миссия Колонизация Марса'
    return render_template('index.html', username=user, title="Супер-пупер-заголовок")


@app.route("/index")
def index():
    user = 'И на Марсе будут яблони цвести!'
    return render_template('index.html', username=user, title="Супер-пупер-заголовок")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
