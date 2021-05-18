# packages
import discord #discord library
import os
from discord.ext import commands #commands


TOKEN = "YOUR TOKEN HERE"
GITHUB = "https://www.github.com/ahoodatheguy/fujiSan"
VERSION = "Beta 1.1.2"
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


@client.event
async def on_disconnect():
	print("bot has disconnected")

#aboutme command
@client.command(name="aboutme") #run run if prefix + "aboutme" is sent
async def aboutme(context):
	print("bot info was requested")
	aboutEmbed = discord.Embed(title="Fuji-San", description="A work in progress discord bot.", color=0xffb7c5) #basic embed structure. color is self explanatory. make sure to use hexadecimal code.
	aboutEmbed.add_field(name="Github: ", value=GITHUB, inline=False)
	aboutEmbed.add_field(name="Version:", value=VERSION, inline=False)
	aboutEmbed.set_author(name="ahoodatheguy", url=TWITTER, icon_url="https://pbs.twimg.com/profile_images/1369100469075853314/cjg-yHFL_400x400.jpg")
	aboutEmbed.set_footer(text="ありがとう")
	channel = context.message.channel #assigns the channel where the message is sent to variable channel
	await context.reply(embed=aboutEmbed) #send embed

@client.command(name="socials")
async def credits(context):
	print("Socials were requested")
	channel = context.message.channel
	socialsEmbed = discord.Embed(title="Social Media", description="You can find me here.", color=0xffb7c5)
	#Replace my socials with yours
	socialsEmbed.add_field(name="Twitch:", value=TWITCH, inline=False)
	socialsEmbed.add_field(name="Twitter:", value=TWITTER, inline=False)
	socialsEmbed.add_field(name="Youtube:", value=YOUTUBE)
	await context.reply(embed=socialsEmbed)

# Connect to server and run bot
client.run(TOKEN)
