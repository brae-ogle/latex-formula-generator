import requests
import json
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
def fromUSD(code, money, data):
    return round(money*data[code],2)
def toUSD(code, money, data):
    return round(money/data[code],2)

def api_call():
    configure()
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_dBYhjjYsR3cxa8MFX77yhwAshEh1CLxiTwRnoIuD&appid={os.getenv('api_key')}"
    api_respose = requests.get(url)
    data = {}
    if api_respose.status_code == 200:
        data_bad_format = api_respose.json()
        data = data_bad_format['data']
    else:
        print("fail")
    return data