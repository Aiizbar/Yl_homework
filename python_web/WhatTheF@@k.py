import json

from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_very_very_secret_key'


@app.route("/")
@app.route("/<username>")
def index(username=''):
    return render_template('NewBase.html', username=username, title="Супер-пупер-заголовок")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')