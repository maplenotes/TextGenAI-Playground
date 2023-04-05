import json
from logging import getLogger, config
import os

from fastapi import FastAPI, Response
from pydantic import BaseModel

import inference 
import staticfile

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


@app.get("/static/{file_name}")
def static(file_name: str):
    if ".." in file_name:
        return Response(content="Forbidden", status_code=403)

    html, media_type = staticfile.get_staticfile(file_name)
    return Response(content=html, media_type=media_type)


### /inference API request
class PormptRequest(BaseModel):
    prompt: str

@app.post("/inference")
def inference_api(req: PormptRequest):
    result = inference.inference(req.prompt)
    return {"answer": result}
