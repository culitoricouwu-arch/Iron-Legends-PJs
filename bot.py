import json
import random
import requests
import os

WEBHOOK = os.environ["WEBHOOK"]

with open("characters.json", encoding="utf-8") as f:
    data = json.load(f)

chance = data["chance"]

if random.randint(1,100) > chance:
    print("Nadie habló hoy.")
    quit()

personaje = random.choice(data["characters"])

mensaje = random.choice(personaje["messages"])

requests.post(
    WEBHOOK,
    json={
        "username": personaje["name"],
        "avatar_url": personaje["avatar"],
        "content": mensaje
    }
)

print(personaje["name"])
print(mensaje)
