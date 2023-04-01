import json
from logging import getLogger, config
import os

from fastapi import FastAPI, Response


if not os.path.isdir("logs"):
	os.mkdir("logs")
with open(os.path.join("logconfig.json"), 'r') as f:
    log_conf = json.load(f)

config.dictConfig(log_conf)
logger = getLogger("app")

logger.info("start server")

app = FastAPI()

@app.get("/")
def index():
    html = ""
    with open("static/index.html") as f:
        html = f.read()
    return Response(content=html, media_type="text/html")
