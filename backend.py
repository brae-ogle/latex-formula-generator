import requests
import json
from dotenv import load_dotenv
import os

# def configure():
#     load_dotenv()
# def fromUSD(code, money, data):
#     return round(money*data[code],2)
# def toUSD(code, money, data):
#     return round(money/data[code],2)

# def api_call():
#     configure()
#     url = f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_dBYhjjYsR3cxa8MFX77yhwAshEh1CLxiTwRnoIuD&appid={os.getenv('api_key')}"
#     api_respose = requests.get(url)
#     data = {}
#     if api_respose.status_code == 200:
#         data_bad_format = api_respose.json()
#         data = data_bad_format['data']
#     else:
#         print("fail")
#     return data



from openai import OpenAI

def configure():
    load_dotenv()

def api_call():
    configure()
    #url = f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_dBYhjjYsR3cxa8MFX77yhwAshEh1CLxiTwRnoIuD&appid={os.getenv('api_key')}"
    from huggingface_hub import hf_api
    import requests

    API_TOKEN = os.getenv('api_key')
    MODEL_ID = "distilbert-base-uncased-distilled-squad"  # Example model

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
    }
    

    data = {
        "inputs": "What is the capital of France?",
    }

    # response = requests.post(
    #     f"https://api-inference.huggingface.co/models/{MODEL_ID}",
    #     headers=headers,
    #     json=data,
    # )
    
    response = requests.get("https://api-inference.huggingface.co/models/{MODEL_ID}", headers=headers, json=data)

    if response.status_code == 200:
        print(response.json())
    else: 
        print(f"error {response.status_code}")

api_call()