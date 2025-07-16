from langchain_ollama.chat_models import ChatOllama
import requests
import json

OLLAMA_URL = "https://ollama.ai/library"

def get_models() -> list:
    thelist = requests.get(OLLAMA_URL+"/api/tags")
    jsondata = thelist.json()
    result = list()

    for model in jsondata["models"]:
        result.append(model["model"])

    return result