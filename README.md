# Pseudo Webhook

A pseudo Reddit-Discord webhook program, created by turtle (github.com/trungams). This program is configured to check a subreddit every few seconds and send an update to the destination URL specified in the config.ini file. The destination is supposed to be a Discord channel but you can change it to your web application.


## Requirements:
   - Python3
   - [asyncio](https://docs.python.org/3/library/asyncio.html)
   - [aiohttp](https://aiohttp.readthedocs.io/en/stable/)
   - [configparser](https://docs.python.org/3/library/configparser.html)


## Installation & Run:
  ```
  git clone https://github.com/trungams/reddit2discord-pseudo-webhook.git
  cd reddit2discord-pseudo-webhook
  python3 -m pip install --user -r requirements.txt
  python3 main.py
  ```
