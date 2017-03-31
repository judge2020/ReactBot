#!/usr/bin/python
# python 3
# requires https://github.com/Rapptz/discord.py / "pip install discord.py"
# licensed under the MIT license. For more information view LICENSE.md

import discord
import asyncio
import os.path
import re
import sys
from pathlib import Path

# CONFIG START -------
# NOTE: unicode emojis need to be in escape sequences, copy them from emojipedia.org
# use 'name:emojiID' for custom emoji
channelids = {
    '159020861708435457': ['\U00002764', '\U0001F44D', '\U0001F44C', '\U0001F44E', 'dust:245699991761321984'],
    '264843760079339530': ['\U00002764', '\U0001F44D', '\U0001F44C', '\U0001F44E', 'dust:245699991761321984'],
    '267062314446880771': ['\U00002764', '\U0001F44D', '\U0001F44C', '\U0001F44E', 'dust:245699991761321984']
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
# CONFIG END -------


client = discord.Client()


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
            if value in message.content:
                print('excluded above message from reactions')
                return

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


def Main():
    try:
        client.run(token)
    except:
        Main()

if os.path.exists('token.txt'):
    tokenfile = open('token.txt', 'r')
    token = tokenfile.read()
    tokenfile.close()
    Main()
else:
    token = input('Please input token: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    Main()
