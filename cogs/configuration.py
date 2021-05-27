from cogs.moderation import moderation
import discord
import json
from discord.ext import commands

class configuration(commands.Cog):
	def __init__(self, client):
		self.client = client

	
	# set twitter handle to be used in socials command
	@commands.command()
	@commands.has_permissions(manage_guild=True)
	async def settwitter(self, context, twitter):
		with open('jsons/socials.json', 'r') as social_file:
			data = json.load(social_file)
		data['TWITTER'] = 'https://' + twitter
		with open('jsons/socials.json', 'w') as social_file:
			json.dump(data, social_file, indent=4)
		print(f'{context.message.author} set twitter to https://{twitter}')
		await context.reply(f'Set twitter to https://{twitter}')
	
	# Set yotuube handle to be used in socials command
	@commands.command()
	@commands.has_permissions(manage_guild=True)
	async def setyoutube(self, context, youtube):
		with open('jsons/socials.json', 'r') as social_file:
			data = json.load(social_file)
		data['YOUTUBE'] = 'https://' + youtube
		with open('jsons/socials.json', 'w') as social_file:
			json.dump(data, social_file, indent=4)
		print(f'{context.message.author} set youtube to https://{youtube}')
		await context.reply(f'Set youtube to https://{youtube}')
	
	# Set twitch handle to be used in twitch command
	@commands.command()
	@commands.has_permissions(manage_guild=True)
	async def settwitch(self, context, twitch):
		with open('jsons/socials.json', 'r') as social_file:
			data = json.load(social_file)
		data['TWITCH'] = 'https://' + twitch
		with open('jsons/socials.json', 'w') as social_file:
			json.dump(data, social_file, indent=4)
		print(f'{context.message.author} set twitch to https://{twitch}')
		await context.reply(f'Set twitch to https://{twitch}')




def setup(client):
	client.add_cog(configuration(client))
