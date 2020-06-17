from flask import Flask,render_template
from api import *
app =  Flask(__name__)


@app.route('/')
def index():
    quote = api()
    return render_template("index.html",quote=quote)
