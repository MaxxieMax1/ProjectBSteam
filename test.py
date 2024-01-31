import json
import pandas as pd

with open('game_data.json', 'r') as file:
    data = json.load(file)

df = pd.DataFrame(data)

def zoek_game(query, games):
    resultaten = []
    for game in games:
        if query.lower() in game["name"].lower():
            resultaten.append(game)
    return resultaten


while True:
    zoekterm = input("Als je wil stoppen typ je exit. Als je iets wil opzoeken typ je wat in\nGeef een zoekterm in: ")
    if zoekterm == 'exit'.lower():
        break
    resultaten = zoek_game(zoekterm, data)
    print(f"Resultaten voor {zoekterm}:\n")
    for resultaat in resultaten:
        print(resultaat["name"])
        print(
            f"Prijs: {resultaat['price']}, Positieve beoordelingen: {resultaat['positive_ratings']}, Genre: {resultaat['genres']}")
        print("-" * 60)