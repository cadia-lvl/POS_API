# -*- coding: utf-8 -*-
import requests
import json

LOC="/tagger"
#LOC="/process/service"

r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content": "Þetta er setning. Og önnur!"})

print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))



r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content": "Hvað heitir þú? Ég heiti Jón."}) 
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))


r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content": "Ásgeir, Jón og María fóru í göngutúr."}) 
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))
