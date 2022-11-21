# request take a data on youtube api
import requests
import json
import csv

# recupere le fichier JSON
url = "https://youtube.googleapis.com/youtube/v3/commentThreads?key=AIzaSyAx6esIx6mqxrGsuZ0RE3uGOsKvNRAzJJg&part" \
      "=snippet, replies&videoId=CmgyUYCibwA&maxResults=100"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
requests = response.json()

with open("JSON_f.json", "w") as JSON_PATH:
    json.dump(requests, JSON_PATH, indent=6)

JSON_PATH.close()

