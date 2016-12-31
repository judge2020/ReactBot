#python 3
#requires https://github.com/Rapptz/discord.py / "pip install discord.py"
#licensed under the MIT license. For more information view LICENSE.md

import discord
import asyncio
import os.path


#CONFIG START -------
channelids = {
'123456789': [':thinking:', ':upside_down:'], 
'987654321': [':smile:', ':forgot_others:']
}
userids = {
'userid1': [':antoher:', ':someother_emoji:'], 
'userid2': [':andanotherone:', ':another_one:']
}
regexes = {'regexpattern1': [':emoji9:', ':emoji10:'], 
'pattern2': [':emoji11:', ':emoji12']
}
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
		for key, value in userids:
			print("add reaction")
	except:
		print("Unexpected error:", sys.exc_info()[0])

if token:
	client.run(token)
else:
	client.run(input('Please input token: '))
#python 3
#requires https://github.com/Rapptz/discord.py / "pip install discord.py"
#licensed under the MIT license. For more information view LICENSE.md

import discord
import asyncio
import os.path


#CONFIG START -------
channelids = {
'123456789': [':thinking:', ':upside_down:'], 
'987654321': [':smile:', ':forgot_others:']
}
userids = {
'userid1': [':antoher:', ':someother_emoji:'], 
'userid2': [':andanotherone:', ':another_one:']
}
regexes = {'regexpattern1': [':emoji9:', ':emoji10:'], 
'pattern2': [':emoji11:', ':emoji12']
}
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
		for key, value in userids:
			print("add reaction")
	except:
		print("Unexpected error:", sys.exc_info()[0])

if token:
	client.run(token)
else:
	client.run(input('Please input token: '))
