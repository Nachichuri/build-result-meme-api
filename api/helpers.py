import requests


def get_latest_version() -> str:
    """
    Fetches the latest version tag of the 'build-result-meme-api' repository from GitHub.

    Returns:
        str: The latest version tag if successful, otherwise 'N/A'.
    """
    try:
        response = requests.get(
            "https://api.github.com/repos/nachichuri/build-result-meme-api/releases/latest"
        )
        response.raise_for_status()

        return response.json().get("tag_name")

    except requests.RequestException:
        return "N/A"


def get_resized_gif(frames, size):
    """
    Resize each frame of a GIF to the specified dimensions.

    Args:
        frames (list[PIL.Image.Image]): List of PIL Image objects representing frames of a GIF.
        size (tuple[int, int]): A tuple containing the desired width and height for resizing.

    Yields:
        PIL.Image.Image: Resized frames of the GIF.
    """
    for frame in frames:
        thumbnail = frame.copy()
        thumbnail.thumbnail(size)
        yield thumbnail
