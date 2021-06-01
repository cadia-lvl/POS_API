# -*- coding: utf-8 -*-
import requests

r = requests.post("http://localhost:8080/tagger", params={"text": "Þetta er setning. Og önnur!"})
exp = b'[[["\xc3\x9eetta","fahen"],["er","sfg3en"],["setning","nven"],[".","pl"]],[["Og","c"],["\xc3\xb6nnur","foven"],["!","pl"]]]'
if r.content != exp:
    print("The response did not match")
print(r.content)
print(exp)
