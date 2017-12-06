#!/usr/bin/python
# python 3
# requires https://github.com/Rapptz/discord.py / "pip install discord.py"
# licensed under the MIT license. For more information view LICENSE.md

import discord
import asyncio
import os.path
import re
import sys
import subprocess
import time
from pathlib import Path
from imgurpython import ImgurClient
import config
import urllib3
import certifi
from webhooks import webhook
from webhooks.senders import targeted
# CONFIG START -------
# NOTE: unicode emojis need to be in escape sequences, copy them from emojipedia.org
# use 'name:emojiID' for custom emoji
channelids = {
    '159020861708435457': ['\U00002764', '\U0001F44D', '\U0001F44C', '\U0001F44E', 'dust:245699991761321984'],
    '264843760079339530': ['\U00002764', '\U0001F44D', '\U0001F44C', '\U0001F44E', 'dust:245699991761321984'],
    '267062314446880771': ['\U00002764', '\U0001F44D', '\U0001F44C', '\U0001F44E', 'dust:245699991761321984'],
    '285072438625042432': ['✅', '❌']
}
userids = {
    # '77542916213444608': ['thinking', 'upside_down'],
    # 'userid2': ['smile', 'upside_down']
}
regexes = {
    # 'regexpattern1': ['smile', 'upside_down'],
    # 'pattern2': ['smile', 'upside_down']
}
exclusions = [
    '(x)',
    '(no-reactions)'
]

startswithexclusion = '`'

statuskeyword = 'Ping'

updateKeywords = {
    # 'userid': 'keyword',
    '77542916213444608': 'updateReact'
}


reactOwnMatch = False

uploadChannels = [
    '159020861708435457',
    '264843760079339530'
]
# CONFIG END -------


client = discord.Client()

iclient = ImgurClient(config.client_id, config.client_secret)

def file_len(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    try:
        print(message.content)
        for value in exclusions:
            if value in message.content or message.content.startswith(startswithexclusion):
                print('excluded message "'+ message.content + '" from reactions')
                return

        if message.channel.id in uploadChannels:
            for value in message.attachments:
                print('Uploading image!' + message.channel.id)
                result = iclient.upload_from_url(value['url'])
                for url in config.webhooks:
                    basic(url=url, imageurl=result['link'])
                print(result['link'])
                urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()).request('GET', config.server_endpoint + "?key=" +
                                                                        config.server_secret +
                                              "&url=" + result['link'])

        if message.content == statuskeyword:
            await client.send_message(message.channel, 'Pong - ReactBot ' + str(file_len('ReactBot.py')))
            print('Pong - ReactBot ' + str(file_len('ReactBot.py')))

        for key, value in updateKeywords.items():
            if message.author.id == key and value == message.content:
                await client.send_message(message.channel, 'Trying to update (lines in file ' + str(file_len('ReactBot.py')) + ')')
                print('Trying to update (lines in file ' + str(file_len('ReactBot.py')) + ')')
                subprocess.call(['./update.sh'])

        for key, value in userids.items():
            print(message.author.id)
            if message.author.id == key:
                for emoji in value:
                    print('Adding emoji to message: "' + message.content + '"')
                    await client.add_reaction(message, emoji)

        for key, value in channelids.items():
            if message.channel.id == key:
                for emoji in value:
                    print('Adding emoji to message: "' + message.content + '"')
                    await client.add_reaction(message, emoji)

        for key, value in regexes.items():
            if re.match(key, message.content):
                for emoji in value:
                    print('Adding emoji to message: "' + message.content + '"')
                    await client.add_reaction(message, emoji)
    except:
        print('unable to add emoji')
        raise

@webhook(sender_callable=targeted.sender)
def basic(url, imageurl):
    return {"content": imageurl}

def Main():
    try:
        client.run(token)
    except:
        print('crashed')
        time.sleep(3)
        Main()



token = config.token
Main()
