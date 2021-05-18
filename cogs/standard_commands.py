import discord
from discord import client
from discord.ext import commands

VERSION = "Beta 1.2.0"
TWITTER = "https://twitter.com/freeahooda"
YOUTUBE = "youtube.com/channel/UCGcwxAVTRuHmrFrI8cwiC3Q"
TWITCH = "twitch.tv/ahoodatheguy"



class standard(commands.Cog):
	def __init__(self, client):
		self.client = client

	# help command
	@commands.command()
	async def help(self, context):
		print('help was requested')
		helpEmbed = discord.Embed(title='Fuji-San commands', description='Commands that you can use in this server', color=0xffb7c5)
		helpEmbed.add_field(name='socials', value='prints social media of the moderator', inline=False)
		helpEmbed.add_field(name = 'aboutme', value="get info about the bot and it's creator", inline=False)
		
		# Role-specific help entries
		if commands.has_permissions(manage_messages=True):
			helpEmbed.add_field(name='clear <amount>', value='delete specified amount of messages (default is 5)', inline=False)
		if commands.has_permissions(ban_members=True):
			helpEmbed.add_field(name='ban <user>', value='ban specified user', inline=False)
			helpEmbed.add_field(name='vindicate <user#12345>', value='unban specified user', inline=False)
		if commands.has_permissions(kick_members=True):
			helpEmbed.add_field(name = 'kick <user>', value='kick specified user', inline=False)
		await context.reply(embed=helpEmbed)

	# about me command
	@commands.command()
	async def aboutme(self, context):
		print('bot info was requested')
		aboutEmbed = discord.Embed = discord.Embed(title='Fuji-San', description='A work in progress discord bot', color=0xffb7c5)
		aboutEmbed.add_field(name='Github: ', value='https://github.com/ahoodatheguy/fujiSan', inline=False)
		aboutEmbed.add_field(name='Version: ', value=VERSION, inline=False)
		aboutEmbed.set_author(name='ahoodatheguy', url=TWITTER, icon_url='https://pbs.twimg.com/profile_images/1369100469075853314/cjg-yHFL_400x400.jpg')
		aboutEmbed.set_footer(text='ありがとう')
		await context.reply(embed=aboutEmbed)

	# socials command
	@commands.command()
	async def socials(self, context):
		print('socials were requested')
		socialsEmbed = discord.Embed(title='Social Media: ', description='You can find me here.', color=0xffb7c5)
		#Replace my socials with yours
		socialsEmbed.add_field(name='Twitch: ', value=TWITCH, inline=False)
		socialsEmbed.add_field(name='Twitter: ', value=TWITTER, inline=False)
		socialsEmbed.add_field(name='Youtube: ', value=YOUTUBE, inline=False)
		await context.reply(embed=socialsEmbed)


def setup(client):
	client.add_cog(standard(client))
