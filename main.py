import requests
import json
from models import *
from flask import Flask, render_template, flash, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    getPictureFromNASA("test")
    return "Test"

@app.route('/result', methods = ['GET', 'POST'])
def result():
    url = getPictureFromNASA("test")
    return render_template("result.html" , url=url)


if __name__ == "__main__":
    app.run(debug=True)
