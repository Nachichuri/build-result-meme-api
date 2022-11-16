import requests


def get_latest_version():
    response = requests.get(
        "https://api.github.com/repos/nachichuri/build-result-meme-api/releases/latest"
    )

    if response.status_code != 200:
        return "N/A"

    return response.json()["tag_name"]


api_description = """
Yet another free public API, this time it will return a meme to illustrate the result of your CI/CD pipeline 🦑

#### How it works

There are three endpoints available:
* [Success](https://build-result-meme.com/success) (https://build-result-meme.com/success)
* [Fixed](https://build-result-meme.com/fixed) (https://build-result-meme.com/fixed)
* [Failure](https://build-result-meme.com/failure) (https://build-result-meme.com/failure)

The returned image will always have a max width and/or height of 500px.

Each endpoint can also take an integer as an argument, which will set the max height and width of the image to the given value. For example:
* [https://build-result-meme.com/success/200](https://build-result-meme.com/success/200) if the original meme was 1366x720px, the returned meme will be 200x112px.

#### How to use it

You can use it in multiple ways:
* ✉️ Jenkins Email
* 🪝 Messaging webhooks (Slack, Discord)
* 📝 Markdown files (using _\!\[ ]\(https://...)_)
* 🤯 Pretty much anywhere you want!

#### How to contribute

Did you just come up with the **most hilarious** pipeline-related meme ever? You can either contribute by [creating a pull request](https://github.com/firstcontributions/first-contributions) to [this API's public repo](https://github.com/Nachichuri/build-result-meme-api), or [contact the maintainer](mailto:nachichuri@gmail.com) with the meme so we can just add it!
"""
