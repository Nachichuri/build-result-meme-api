# 🏗️ build-result-meme-api

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Nachichuri/build-result-meme-api/build.yaml?style=flat-square)
![](https://img.shields.io/github/license/nachichuri/build-result-meme-api?color=orange&style=flat-square)

Yet another meme webpage. This time, you will get a random meme to illustrate the result of your CI/CD pipelines 🦑

#### How it works

There are 3 endpoints available:
* [Success](https://build-result-meme.com/success) (https://build-result-meme.com/success)
* [Fixed](https://build-result-meme.com/fixed) (https://build-result-meme.com/fixed)
* [Failure](https://build-result-meme.com/failure) (https://build-result-meme.com/failure)

> By default, the returned meme will always have a max width and/or height of 500px.

Each endpoint can also take an integer as an optional path, which will set the max height and width of the image to the given value. For instance:
* [https://build-result-meme.com/success/200](https://build-result-meme.com/success/200) if the original meme was 1366x720px, the returned meme will be 200x112px.

#### How to use it

You can use it in multiple ways:
* ✉️ Email notifications
* 🪝 Messaging webhooks (Slack, Discord)
* 📝 Markdown files (using _\!\[ ]\(https://...)_)
* 🤯 Pretty much anywhere you want!

#### How to contribute

Did you just come up with the **most hilarious** pipeline-related meme ever? You can either contribute by [creating a pull request](https://github.com/firstcontributions/first-contributions) to this repo, or [send the meme to the mantainer](mailto:nachichuri@gmail.com) so it can be added to the collection!
