import datetime
import requests
import json

DB = "../DATABASE/"
STATIC_HOST = 'https://assets.mist-train-girls.com/production-client-web-static'

FILE = []

def retrieve_file():
    global FILE
    with open("file_list.txt", 'r', encoding='utf-8') as file:
        for line in file:
            FILE = FILE + [line.strip()]

def main():
    
    for file in FILE:
        link = f"{STATIC_HOST}/MasterData/" + file
        db = None
        res = requests.get(link)
        res.raise_for_status()  # raises exception when not a 2xx response
        if res.status_code != 204:
            try:
                db = res.json()
            except requests.exceptions.JSONDecodeError:
                db = json.loads(res.content.decode('utf-8-sig'))
        
        with open(DB + file, "w", encoding = "utf8") as wfile:
            json.dump(db, wfile, indent=4)
            wfile.truncate()

retrieve_file()
main()