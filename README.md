# Pseudo Webhook

A pseudo Reddit-Discord webhook program, created by turtle (github.com/trungams). This program is configured to check a subreddit every few seconds and send an update to the destination URL specified in the config.ini file. The destination is supposed to be a Discord channel but you can change it to your web application.


## Requirements:
   - [Python3](https://www.python.org/)
   - [asyncio](https://docs.python.org/3/library/asyncio.html)
   - [aiohttp](https://aiohttp.readthedocs.io/en/stable/)
   - [configparser](https://docs.python.org/3/library/configparser.html)


## Installation & Run:
  Remember to create a webhook on your Discord server and change the values in config.ini before running this program. [Check this guide](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks) if you don't know how to do that.

  ```
  git clone https://github.com/trungams/reddit2discord-pseudo-webhook.git
  cd reddit2discord-pseudo-webhook
  python3 -m pip install --user -r requirements.txt
  python3 main.py
  ```
