import json
from logging import getLogger, config
import os

from fastapi import FastAPI, Response
from pydantic import BaseModel

import inference 

if not os.path.isdir("logs"):
	os.mkdir("logs")
with open(os.path.join("logconfig.json"), 'r') as f:
    log_conf = json.load(f)

config.dictConfig(log_conf)
logger = getLogger("app")

logger.info("start server")

app = FastAPI()

inference.initialize()

@app.get("/")
def index():
    html = ""
    with open("static/index.html") as f:
        html = f.read()
    return Response(content=html, media_type="text/html")


### /inference API request
class PormptRequest(BaseModel):
    prompt: str

@app.post("/inference")
def inference_api(req: PormptRequest):
    result = inference.inference(req.prompt)
    return {"answer": result}
