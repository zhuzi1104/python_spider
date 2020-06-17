import json
import requests


def parse(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
    }
    response = requests.get(url, headers=headers).json()
    response = json.dumps(response, ensure_ascii=False)
    yield response