import discord
from discord.ext import commands



class easter_eggs(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def neofetch(self, context):
		print('running neofetch')
		server = context.message.guild.name
		neofetch = open('neofetch/boilerplate.txt', 'r')
		await context.reply(f'```{neofetch.read()}```')


def setup(client):
	client.add_cog(easter_eggs(client))
