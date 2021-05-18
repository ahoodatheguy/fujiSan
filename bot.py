# packages
import discord #discord library
import os
from discord.ext import commands #commands


TOKEN = "ODMyMzcwODE5OTkyNzgwODEw.YHizvA.dw2f1HL3vnlEj4ojNpJf-0BC82U"
GITHUB = "https://www.github.com/ahoodatheguy/fujiSan"
VERSION = "Beta 1.2.0"
TWITTER = "https://twitter.com/freeahooda"
YOUTUBE = "youtube.com/channel/UCGcwxAVTRuHmrFrI8cwiC3Q"
TWITCH = "twitch.tv/ahoodatheguy"
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
client.run(TOKEN)
