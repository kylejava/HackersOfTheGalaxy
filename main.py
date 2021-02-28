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
        requestedDate = request.form['date']
        yourName = request.form['yourName']
        yourPartnerName = request.form['yourPartnerName']
        date = yourName + " & "+ yourPartnerName + ", these are what the stars looked like on "+ requestedDate
        url = getPictureFromNASA(requestedDate)
    return render_template("result.html" , url=url, date=date)


if __name__ == "__main__":
    app.run(debug=True)
