import os
import random
from io import BytesIO

from fastapi import FastAPI
from fastapi.responses import RedirectResponse, StreamingResponse
from PIL import Image

from api.helpers import api_description, get_latest_version

app = FastAPI(
    title="🏗️ build-result-meme-api",
    description=api_description,
    version=get_latest_version(),
    contact={
        "name": "GitHub",
        "url": "https://github.com/Nachichuri/build-result-meme-api",
    },
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)


@app.get("/", response_class=RedirectResponse, status_code=303, include_in_schema=False)
async def docs():
    return "/docs"


@app.get("/success", tags=["memes"])
async def success():
    source = Image.open(
        f'api/assets/success/{random.choice(os.listdir("api/assets/success/"))}'
    )
    source.thumbnail((500, 500))
    source = source.convert("RGB")

    image = BytesIO()
    source.save(image, "JPEG")
    image.seek(0)

    return StreamingResponse(image, media_type="image/jpeg")


@app.get("/success/{size}", tags=["custom size"])
async def success_custom(size):
    try:
        size = int(size)
    except Exception:
        size = 500

    source = Image.open(
        f'api/assets/success/{random.choice(os.listdir("api/assets/success/"))}'
    )
    source.thumbnail((size, size))
    source = source.convert("RGB")

    image = BytesIO()
    source.save(image, "JPEG")
    image.seek(0)

    return StreamingResponse(image, media_type="image/jpeg")


@app.get("/fixed", tags=["memes"])
async def fixed():
    source = Image.open(
        f'api/assets/fixed/{random.choice(os.listdir("api/assets/fixed/"))}'
    )
    source.thumbnail((500, 500))
    source = source.convert("RGB")

    image = BytesIO()
    source.save(image, "JPEG")
    image.seek(0)

    return StreamingResponse(image, media_type="image/jpeg")


@app.get("/fixed/{size}", tags=["custom size"])
async def fixed_custom(size):
    try:
        size = int(size)
    except Exception:
        size = 500

    source = Image.open(
        f'api/assets/fixed/{random.choice(os.listdir("api/assets/fixed/"))}'
    )
    source.thumbnail((size, size))
    source = source.convert("RGB")

    image = BytesIO()
    source.save(image, "JPEG")
    image.seek(0)

    return StreamingResponse(image, media_type="image/jpeg")


@app.get("/failure", tags=["memes"])
async def failure():
    source = Image.open(
        f'api/assets/failure/{random.choice(os.listdir("api/assets/failure/"))}'
    )
    source.thumbnail((500, 500))
    source = source.convert("RGB")

    image = BytesIO()
    source.save(image, "JPEG")
    image.seek(0)

    return StreamingResponse(image, media_type="image/jpeg")


@app.get("/failure/{size}", tags=["custom size"])
async def failure_custom(size):
    try:
        size = int(size)
    except Exception:
        size = 500

    source = Image.open(
        f'api/assets/failure/{random.choice(os.listdir("api/assets/failure/"))}'
    )
    source.thumbnail((size, size))
    source = source.convert("RGB")

    image = BytesIO()
    source.save(image, "JPEG")
    image.seek(0)

    return StreamingResponse(image, media_type="image/jpeg")
