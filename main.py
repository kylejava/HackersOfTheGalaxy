import requests
import json
from models import *
from flask import Flask, render_template, flash, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if(request.method == 'POST'):
        date = request.form['date']
        url = getPictureFromNASA(date)
    return render_template("result.html" , url=url)


if __name__ == "__main__":
    app.run(debug=True)
