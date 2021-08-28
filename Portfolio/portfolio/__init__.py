from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'bb2f777a52780c206b7bcaeb8fd1f487'

from portfolio import routes