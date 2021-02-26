import json
import requests
from pprint import pprint
from keys import *

def getPictureFromNASA(date):
    date = "2014-04-22"
    url = getURL(date)
    response = requests.get(url)
    data = response.json()
    return(data[0]['hdurl'])
