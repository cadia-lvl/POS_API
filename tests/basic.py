# -*- coding: utf-8 -*-
import requests
import json

LOC="/tagger"
#LOC="/process/service"

r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content": "Þetta er setning. Og önnur!"})
json.loads(r.content.decode("utf-8"))

print("OUT:",r.content.decode("utf-8"))
