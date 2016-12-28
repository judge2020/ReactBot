#python 3
#requires https://github.com/Rapptz/discord.py / "pip install discord.py"
#licensed under the MIT license. For more information view LICENSE.md

import discord
import asyncio
import os.path


#CONFIG START -------
channelids = []
userids = []
regexes = []
token = ''
#CONFIG END -------


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
		
	except:
		print("Unexpected error:", sys.exc_info()[0])



if token:
	client.run(token)
else:
	client.run(input('Please input token: '))
