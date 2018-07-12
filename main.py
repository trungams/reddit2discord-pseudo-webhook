#!/usr/bin/python3

import asyncio
import aiohttp
import configparser

base_url = subreddit = subreddit_url = destination_url = cache_file = frequency = None

def config():
    global base_url, subreddit, subreddit_url, destination_url, cache_file, frequency
    config = configparser.ConfigParser()
    config.read('config.ini')
    base_url = config['URLs']['base_url']
    subreddit = config['URLs']['subreddit']
    subreddit_url = 'https://www.reddit.com/r/' + subreddit + '/new.json?sort=new'
    destination_url = config['URLs']['destination_url']
    cache_file = config['misc']['cache_file']
    frequency = int(config['misc']['frequency'])


async def fetch_sub_json(session):
    async with session.get(subreddit_url) as response:
        return await response.json()


def save_cache(posts):
    with open(cache_file, 'w') as f:
        for post in posts:
            f.write(post['data']['id'] + ' ')


def get_cache():
    with open(cache_file, 'r') as f:
        post_ids = f.read().split()
        return post_ids


async def make_notif(session, post_json):
    await session.post(destination_url,
        json = {'content': base_url + post_json['data']['permalink']}
    )


async def refresh(session):
    counter = 1
    while True:
        cache = get_cache()
        response = await fetch_sub_json(session)
        posts = response['data']['children']
        for post in posts:
            if post['data']['id'] not in cache:
                await make_notif(session, post)
        save_cache(posts)
        counter += 1
        await asyncio.sleep(frequency)


async def main():
    async with aiohttp.ClientSession() as session:
        await refresh(session)


if __name__ == '__main__':
    config()
    print('A pseudo Reddit-Discord webhook program, created by turtle (github.com/trungams). This program is configured to check the r/{} subreddit every {} seconds and send an update to the destination URL specified in the config.ini file.'.format(subreddit, frequency))
    with open(cache_file, 'a') as f:
        pass
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pending = asyncio.Task.all_tasks(loop=loop)
        gathered = asyncio.gather(*pending, loop=loop)
        try:
            gathered.cancel()
            gathered.exception()
        except:
            pass
    finally:
        loop.close()
