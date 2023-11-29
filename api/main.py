import os
import random
from io import BytesIO

from fastapi import FastAPI
from fastapi.responses import RedirectResponse, StreamingResponse
from PIL import Image, ImageSequence

from api.documentation import api_description
from api.helpers import get_latest_version, get_resized_gif


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
    """
    Redirects the root URL to the '/docs' endpoint with a status code of 303 (See Other).
    """
    return RedirectResponse("/docs")


@app.get("/{status}", include_in_schema=False)
@app.get("/{status}/{size}", tags=["Endpoints"])
async def meme(status: str, size: str = "500") -> StreamingResponse:
    """
    ## Generates and returns a meme image or GIF based on the specified status and size.

    ### Args:\n
    `status (str)`: The category or status of the meme.\n
    `size (str, optional)`: The desired size of the meme. Defaults to "500".

    ### Returns:\n
    `fastapi.responses.StreamingResponse`: A streaming response containing the generated meme.

    ### Raises:\n
    `fastapi.responses.RedirectResponse`: Redirects to the '/docs' endpoint if the specified status is not valid.
    """
    # Check if the specified status exists in the meme assets directory
    if status not in os.listdir("api/assets/"):
        return RedirectResponse("/docs", status_code=303)

    # Attempt to convert the size to an integer; default to 500 if conversion fails
    try:
        size = int(size)
    except ValueError:
        size = 500

    # Form the path to a random image within the specified status directory
    random_image = (
        f'api/assets/{status}/{random.choice(os.listdir(f"api/assets/{status}/"))}'
    )

    # If the randomly chosen image is a GIF, process and return a streaming GIF response
    if random_image.lower().endswith("gif"):
        source = Image.open(random_image)
        frames = ImageSequence.Iterator(source)
        frames = get_resized_gif(frames, (size, size))

        processed_gif = next(frames)
        processed_gif.info = source.info
        final_gif = BytesIO()
        processed_gif.save(final_gif, "GIF", save_all=True, append_images=list(frames))
        final_gif.seek(0)

        return StreamingResponse(final_gif, media_type="image/gif")

    # If the randomly chosen image is not a GIF, process and return a streaming JPEG response
    source = Image.open(random_image)
    source.thumbnail((size, size))
    source = source.convert("RGB")

    image = BytesIO()
    source.save(image, "JPEG")
    image.seek(0)

    return StreamingResponse(image, media_type="image/jpeg")


@app.exception_handler(404)
async def custom_404_handler(_, __):
    """
    Custom exception handler for handling 404 Not Found errors.

    Args:
        _: FastAPI request object (not used in the function).
        __: Exception information (not used in the function).

    Returns:
        RedirectResponse: Redirects to the '/docs' endpoint with a status code of 303 (See Other).
    """
    return RedirectResponse("/docs", status_code=303)
