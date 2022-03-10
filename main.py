from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse
from tokenizer import split_into_sentences
from pydantic import BaseModel
from typing import Optional

import torch
import pos


__version__ = 0.1

class TaggerInput(BaseModel):
	type: Optional[str] = "text"
	content: str

app = FastAPI()



# Initialize the tagger
device = torch.device("cpu")  # CPU
tagger: pos.Tagger = torch.hub.load(
	repo_or_dir="cadia-lvl/POS",
	model="tag",
	device=device,
	force_reload=False,
	force_download=False,
)


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

	text = request.content
	sentences = [sentence.split() for sentence in split_into_sentences(text)]
	tags = tagger.tag_bulk(sentences, batch_size=2)
	resp = []
	for sentence, tag in zip(sentences, tags):
		sent = []
		for s,t in zip(sentence, tag):
			sent.append({"content":s,"features":{"tag":t}})
		resp.append({"texts":sent})
	return JSONResponse(content={"response":{"type":"texts","texts":resp}})


#@app.post('/lemmitizer')
#def api_tagger(text : str) -> str:
#	return ""
