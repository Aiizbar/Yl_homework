import json

from flask import Flask, render_template


app = Flask(__name__)




@app.route("/")
def passiv():
    user = 'Миссия Колонизация Марса'
    return render_template('index.html', username=user, title="Супер-пупер-заголовок")


@app.route("/index")
def index():
    user = 'И на Марсе будут яблони цвести!'
    return render_template('index.html', username=user, title="Супер-пупер-заголовок")


@app.route('/countdown')
def countdown():
    countdown_list = [str(x) for x in range(10, 0, -1)]
    countdown_list.append('Пуск!')
    return '</br>'.join(countdown_list)


@app.route('/p')
def promotion():
    countdown_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'По этому, пожалуйста', 'Умри.']
    return '</br>'.join(countdown_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
