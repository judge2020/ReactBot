#!/usr/bin/python
# -*- coding: utf-8 -*-
# python 3
# requires https://github.com/Rapptz/discord.py / "pip install discord.py"
# licensed under the MIT license. For more information view LICENSE.md

import os.path
import re
import time
from typing import TYPE_CHECKING

import discord
from webhooks import webhook
from webhooks.senders import targeted

# CONFIG START -------
#
# Full config in environ coming soon. Also probably a rewrite for Discord.py 1.0.
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
SENTRY_DSN = os.environ.get('SENTRY_DSN', '')
#
# NOTE: unicode emojis need to be in escape sequences, copy them from emojipedia.org
# use 'name:emojiID' for custom emoji
channelids = {
    '159020861708435457': ['\U00002764', '\U0001F44D', '\U0001F44C', '\U0001F44E', 'dust:245699991761321984'],
    '264843760079339530': ['\U00002764', '\U0001F44D', '\U0001F44C', '\U0001F44E', 'dust:245699991761321984'],
    '267062314446880771': ['\U00002764', '\U0001F44D', '\U0001F44C', '\U0001F44E', 'dust:245699991761321984'],
    '386329867404312576': ['✅', '❌']
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

reactOwnMatch = False

# CONFIG END -------

if len(SENTRY_DSN) >= 5:
    import sentry_sdk

    sentry_sdk.init(SENTRY_DSN)


client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message: discord.Message):
    if TYPE_CHECKING:
        message.channel = message.channel  # type: discord.TextChannel
        message.author = message.author  # type: discord.Member
    for value in exclusions:
        if value in message.content or message.content.startswith(startswithexclusion):
            print('excluded message "' + message.content + '" from reactions')
            return

    if message.content == statuskeyword:
        await message.channel.send('Pong - ReactBot')

    for key, value in userids.items():
        if message.author.id == key:
            for emoji in value:
                print('Adding emoji to message: "' + message.content + '"')
                await message.add_reaction(emoji)

    for key, value in channelids.items():
        if message.channel.id == key:
            for emoji in value:
                print('Adding emoji to message: "' + message.content + '"')
                await message.add_reaction(emoji)

    for key, value in regexes.items():
        if re.match(key, message.content):
            for emoji in value:
                print('Adding emoji to message: "' + message.content + '"')
                await message.add_reaction(emoji)


if __name__ == '__main__':
    client.run(DISCORD_TOKEN)
