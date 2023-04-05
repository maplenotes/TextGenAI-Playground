
import os


def get_staticfile(file_name: str):
    media_type = "text/html"
    if file_name.endswith(".html"):
        media_type = "text/html"
    elif file_name.endswith(".js"):
        media_type = "application/javascript"
    elif file_name.endswith(".css"):
        media_type = "text/css"
    elif file_name.endswith(".json"):
        media_type = "application/json"
    elif file_name.endswith(".png"):
        media_type = "image/png"
    elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        media_type = "image/jpg"
    else:
        media_type = "application/octet-stream"

    with open(os.path.join("static", file_name), "rb") as f:
        html = f.read()

    return html, media_type