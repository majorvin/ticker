import requests
import json
import os

ticker = os.environ['ticker']
alphaToken = os.environ['alphaToken']

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&apikey=$" + alphaToken
r = requests.get(url)
body = r.json()

print("------ REPONSE --------")
print(body)

price = ""
date = ""
for x in body:
    if "Time" in x:
        for date in body[x]:
            for p in body[x][date]:
                if "close" in p:
                    price = body[x][date][p]
                    break
            break


closing_price = {
    date: "" + price
}

with open("./data/" + ticker + ".json", "w") as file:
    json.dump(closing_price, file)