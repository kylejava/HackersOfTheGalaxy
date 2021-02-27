import json
import requests
from pprint import pprint
from keys import *

def getPictureFromNASA(date):
    url = getURL(date)
    response = requests.get(url)
    data = response.json()
    return(data[0]['hdurl'])
