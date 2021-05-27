# packages
import discord #discord library
import os
from discord.errors import LoginFailure
from discord.ext import commands #commands
import json

bot_info = open("jsons/bot_info.json", "r")
info = json.load(bot_info)

#Client
client = commands.Bot(command_prefix="!") #the discord bot, also sets prefix
client.remove_command("help") #unbinds the default help command for us to use


@client.event
async def on_ready(): #Excecute when bot joins server
	print("Bot is running!")
	for filename in os.listdir('./cogs'):
		if filename.endswith('.py'):
			try:
				client.load_extension(f'cogs.{filename[:-3]}')
				print(f'cog {filename} loaded')
			except Exception as e:
				print(f'Failed to load {filename}')
				print(e)

# Connect to server and run bot
try:
	client.run(info["TOKEN"])
except LoginFailure:
	print('Failed to login, check if your token is valid')
