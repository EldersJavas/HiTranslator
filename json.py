import json

f = open('db.json')
data = json.load(f)
f.close()

print(data)