from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse
import pos
from tokenizer import split_into_sentences
from pydantic import BaseModel


__version__ = 0.1

class TaggerInput(BaseModel):
    type: Optional[str] = "text"
    content: str

app = FastAPI()

# Initialize the tagger
tagger = pos.Tagger(model_file="tagger-v2.0.0.pt", device="cpu")

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
def api_tagger(request : str) -> str:
    return api_tagger_impl(request.content)


@app.post('/tagger/impl')
def api_tagger_impl(text : str) -> str:
    sentences = [sentence.split() for sentence in split_into_sentences(text)]
    tags = tagger.tag_bulk(sentences, batch_size=2)
    out = []
    for sentence, tag in zip(sentences, tags):
        s = []
        for a, b in zip(sentence, tag):
            s.append([a,b])
        out.append(s)
    return JSONResponse(content=out)


#@app.post('/lemmitizer')
#def api_tagger(text : str) -> str:
#    return ""
