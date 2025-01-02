import requests
import json
import re
from bs4 import BeautifulSoup


def get_request_json(url: str, params: dict | None = None):
    # extract json from url
    if params != None:
        r = requests.get(url, params=params)
    else:
        r = requests.get(url)
    return r.json()

def get_request_text(url: str, params: dict | None = None):
    # extract a javascript variable from the html
    if params != None:
        r = requests.get(url, params=params)
    else:
        r = requests.get(url)
    text = r.text
    return text