import discord
from discord import client
from discord.ext import commands

class standard(commands.Cog):
	def __init__(self, client):
		self.client = client
	@commands.command()
	async def help(self, context):
		print('help was requested')
		helpEmbed = discord.Embed(title='Fuji-San commands', description='Commands that you can use in this server', color=0xffb7c5)
		helpEmbed.add_field(name='socials', value='prints social media of the moderator', inline=False)
		helpEmbed.add_field(name = 'aboutme', value="get info about the bot and it's creator", inline=False)

		if commands.has_permissions(manage_messages=True):
			helpEmbed.add_field(name='clear <amount>', value='delete specified amount of messages (default is 5)', inline=False)
		if commands.has_permissions(ban_members=True):
			helpEmbed.add_field(name='ban <user>', value='ban specified user', inline=False)
			helpEmbed.add_field(name='vindicate <user#12345>', value='unban specified user', inline=False)
		if commands.has_permissions(kick_members=True):
			helpEmbed.add_field(name = 'kick <user>', value='kick specified user', inline=False)
		await context.reply(embed=helpEmbed)
def setup(client):
	client.add_cog(standard(client))
