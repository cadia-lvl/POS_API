# -*- coding: utf-8 -*-
import requests
import json

LOC="/tagger"
#LOC="/process/service"

inp =  "Þetta er setning. Og önnur!"
print("INP:",inp)
r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content":inp})
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))
print()

inp = "Hvað heitir þú? Ég heiti Jón."
print("INP:",inp)
r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content": inp}) 
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))
print()

inp = "Ásgeir, Jón og María fóru í göngutúr."
print("INP:",inp)
r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content": inp}) 
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))
print()

print("############ Error ############")
inp = ""
print("INP:",inp)
r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content": inp}) 
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))
print()

inp = {}
print("INP:",inp)
r = requests.post("http://localhost:8080"+LOC, json=inp) 
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))
print()

inp = {"type":"text"}
print("INP:",inp)
r = requests.post("http://localhost:8080"+LOC, json=inp) 
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))
print()
