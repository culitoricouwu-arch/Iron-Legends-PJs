import json
import random
import requests
import os

WEBHOOK = os.environ["WEBHOOK"]

with open("characters.json", encoding="utf-8") as f:
    data = json.load(f)

if random.randint(1,100) > data["chance"]:
    print("Nadie habló.")
    quit()

personaje=random.choice(data["characters"])
mensaje=random.choice(personaje["messages"])

requests.post(
    WEBHOOK,
    json={
        "username":personaje["name"],
        "avatar_url":personaje["avatar"],
        "content":mensaje
    }
)

print("Publicado:",personaje["name"])
print(personaje["name"])
print(mensaje)
