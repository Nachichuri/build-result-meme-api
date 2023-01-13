import os
import random
from io import BytesIO

from fastapi import FastAPI
from fastapi.responses import RedirectResponse, StreamingResponse
from PIL import Image, ImageSequence

from api.helpers import api_description, get_latest_version, get_resized_gif

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
    random_image = (
        f'api/assets/success/{random.choice(os.listdir("api/assets/success/"))}'
    )

    if random_image[-3:] == "gif":
        source = Image.open(random_image)
        frames = ImageSequence.Iterator(source)
        frames = get_resized_gif(frames, (500, 500))

        processed_gif = next(frames)
        processed_gif.info = source.info
        final_gif = BytesIO()
        processed_gif.save(final_gif, "GIF", save_all=True, append_images=list(frames))
        final_gif.seek(0)

        return StreamingResponse(final_gif, media_type="image/gif")

    source = Image.open(random_image)
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

    random_image = (
        f'api/assets/success/{random.choice(os.listdir("api/assets/success/"))}'
    )

    if random_image[-3:] == "gif":
        source = Image.open(random_image)
        frames = ImageSequence.Iterator(source)
        frames = get_resized_gif(frames, (size, size))

        processed_gif = next(frames)
        processed_gif.info = source.info
        final_gif = BytesIO()
        processed_gif.save(final_gif, "GIF", save_all=True, append_images=list(frames))
        final_gif.seek(0)

        return StreamingResponse(final_gif, media_type="image/gif")

    source = Image.open(random_image)
    source.thumbnail((size, size))
    source = source.convert("RGB")

    image = BytesIO()
    source.save(image, "JPEG")
    image.seek(0)

    return StreamingResponse(image, media_type="image/jpeg")


@app.get("/fixed", tags=["memes"])
async def fixed():
    random_image = f'api/assets/fixed/{random.choice(os.listdir("api/assets/fixed/"))}'

    if random_image[-3:] == "gif":
        source = Image.open(random_image)
        frames = ImageSequence.Iterator(source)
        frames = get_resized_gif(frames, (500, 500))

        processed_gif = next(frames)
        processed_gif.info = source.info
        final_gif = BytesIO()
        processed_gif.save(final_gif, "GIF", save_all=True, append_images=list(frames))
        final_gif.seek(0)

        return StreamingResponse(final_gif, media_type="image/gif")

    source = Image.open(random_image)
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

    random_image = f'api/assets/fixed/{random.choice(os.listdir("api/assets/fixed/"))}'

    if random_image[-3:] == "gif":
        source = Image.open(random_image)
        frames = ImageSequence.Iterator(source)
        frames = get_resized_gif(frames, (size, size))

        processed_gif = next(frames)
        processed_gif.info = source.info
        final_gif = BytesIO()
        processed_gif.save(final_gif, "GIF", save_all=True, append_images=list(frames))
        final_gif.seek(0)

        return StreamingResponse(final_gif, media_type="image/gif")

    source = Image.open(random_image)
    source.thumbnail((size, size))
    source = source.convert("RGB")

    image = BytesIO()
    source.save(image, "JPEG")
    image.seek(0)

    return StreamingResponse(image, media_type="image/jpeg")


@app.get("/failure", tags=["memes"])
async def failure():
    random_image = (
        f'api/assets/failure/{random.choice(os.listdir("api/assets/failure/"))}'
    )

    if random_image[-3:] == "gif":
        source = Image.open(random_image)
        frames = ImageSequence.Iterator(source)
        frames = get_resized_gif(frames, (500, 500))

        processed_gif = next(frames)
        processed_gif.info = source.info
        final_gif = BytesIO()
        processed_gif.save(final_gif, "GIF", save_all=True, append_images=list(frames))
        final_gif.seek(0)

        return StreamingResponse(final_gif, media_type="image/gif")

    source = Image.open(random_image)
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

    random_image = (
        f'api/assets/failure/{random.choice(os.listdir("api/assets/failure/"))}'
    )

    if random_image[-3:] == "gif":
        source = Image.open(random_image)
        frames = ImageSequence.Iterator(source)
        frames = get_resized_gif(frames, (size, size))

        processed_gif = next(frames)
        processed_gif.info = source.info
        final_gif = BytesIO()
        processed_gif.save(final_gif, "GIF", save_all=True, append_images=list(frames))
        final_gif.seek(0)

        return StreamingResponse(final_gif, media_type="image/gif")

    source = Image.open(random_image)
    source.thumbnail((size, size))
    source = source.convert("RGB")

    image = BytesIO()
    source.save(image, "JPEG")
    image.seek(0)

    return StreamingResponse(image, media_type="image/jpeg")
