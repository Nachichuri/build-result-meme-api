import os
import random
from io import BytesIO

from fastapi import FastAPI
from fastapi.responses import RedirectResponse, StreamingResponse
from PIL import Image

app = FastAPI()


@app.get("/", response_class=RedirectResponse, status_code=303)
async def docs():
    return "/docs"


@app.get("/success", response_class=StreamingResponse)
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


@app.get("/success/{size}")
async def success_custom(size):
    try:
        size = int(size)
    except Exception as e:
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


@app.get("/fixed", response_class=StreamingResponse)
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


@app.get("/fixed/{size}")
async def fixed_custom(size):
    try:
        size = int(size)
    except Exception as e:
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


@app.get("/failure", response_class=StreamingResponse)
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


@app.get("/failure/{size}")
async def failure_custom(size):
    try:
        size = int(size)
    except Exception as e:
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
