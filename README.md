# AssasiansBot

A GroupMe Bot used to moderate and enable all interactions for a game of Assasians

### Author

**Daniel Gisolfi** - *All current work* - [dgisolfi](https://github.com/dgisolfi)

## Usage

TODO: Daniel make a usage guide...

## Groupme Bot

A GroupMe bot can be created [here](https://dev.groupme.com/bots) and using the Groupme API can send messages to its assigned group. This particular bot uses a callback URL to be notified of new messages. Once notified the message will be parsed and a response will be created if the `USER_ID` of the sender matches that of the `USER_ID` environment variable.

### Setup

Once a bot is registered with Groupme the following requirements must be specified in the form of environment variables:

* **BOT_ID** - The assigned bot ID by GroupMe.

  Example: `BOT_ID=a6a7a7a7a7a7a7a7a77a7a7`

* **GROUP_ID** - The ID of the Groupme Chat where the bot resides

  Example: `GROUP_ID=0987890987`
* **API_TOKEN** - The api token for the authorized Groupme account

  Example: `API_TOKEN=983u4ritgo0v98ujkorf`

After the environment variables have been set run the Flask server, `python -m AssasiansBot`

