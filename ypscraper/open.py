import json

with open('searches.json','r') as f:
    searches = json.loads(f.read())

print(len(searches))
