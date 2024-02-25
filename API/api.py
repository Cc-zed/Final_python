import requests
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
import os

CHAT_GPT_API= os.getenv("CHAT_GPT_API")


def get_random_duck():
    endpoint = "https://random-d.uk/api/random"
    # endpoint = "https://api.api-ninjas.com/v1/randomimage?category=dog"
    response = requests.get(endpoint)
    data = response.json()
    return data["url"]

def get_chatGPT_response(question):
    url = "https://api.openai.com/v1/chat/completions"
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {CHAT_GPT_API}"}
    data = {"model": "gpt-3.5-turbo","messages": [{"role": "user","content": question}]}
    response = requests.post(url, headers=header, json=data)
    if response.status_code == 200:
        data = response.json()
        return data ['choices'][0]['message']['content']
    else:
        return "Cannt connect to server"