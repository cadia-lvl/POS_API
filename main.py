from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse
from tokenizer import split_into_sentences
from pydantic import BaseModel
from typing import Optional
import traceback

from models import *

__version__ = 0.1

class TaggerInput(BaseModel):
	type: Optional[str] = "text"
	content: str

app = FastAPI()

def error(errors):
    return JSONResponse(content=({"failure":{"errors":[errors]}}))




@app.get('/', response_class=HTMLResponse)
def home() -> str:
	return """
<html>
	<head><title>POS API</title></head>
	<body>
		<h1>POS API Server v{0}</h1>
		<ul><li><a href="/docs">Documentation</a></li></ul>
	</body>
</html>
""".format(__version__)

@app.post('/tagger')
def api_tagger(request : TaggerInput) -> str:
	try:
			text = request.content
			sentences = [sentence.split() for sentence in split_into_sentences(text)]
	except:
		return error({"code":"pos.bad.input", "text":"Bad input", "detail":{'traceback':traceback.format_exc()}})
	try:
		tags = tagger_model.tag_bulk(sentences, batch_size=2)
	except:
		return error({"code":"pos.model.error", "text":"model was unable to tag input", "detail":{'traceback':traceback.format_exc()}})
	resp = []
	for sentence, tag in zip(sentences, tags):
		sent = []
		for s,t in zip(sentence, tag):
			sent.append({"content":s,"features":{"tag":t}})
		resp.append({"texts":sent})
	return JSONResponse(content={"response":{"type":"texts", "texts":resp}})

