import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Kicking
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, user : discord.Member,*, reason = 'reason not given'):
        channel = context.message.channel
        await user.kick(reason=reason)
        if reason == 'reason not given':
            print('user ' + str(user) + ' was kicked')
            await channel.send('**' + str(user) + ' was kicked**')
        else:
            print('user ' + str(user) + ' was kicked for ' + str(reason))
            await channel.send('**' + str(user) + ' was kicked for ' + str(reason) + '**')

    #Banning
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, user : discord.Member,*, reason = 'reason not given'):
        channel = context.message.channel
        await user.ban(reason=reason)
        if reason == 'reason not given':
            print('user ' + str(user) + ' was banned')
            await channel.send('**' + str(user) + ' has been banned**')
        else:
            await channel.send('**' + str(user) + ' has been banned for ' + str(reason) + '**')
            print('user ' + str(user) + ' was banned for ' + str(reason))

    #Unbanning
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def vindicate (self, context,*, user):
        channel = context.message.channel
        banned_users = await context.guild.bans()
        discord_name, discord_discriminator = user.split('#')

        for banned in banned_users:
            user = banned.user
            if (user.name, user.discriminator) == (discord_name, discord_discriminator):
                await context.guild.unban(user)
                print(user.name + user.discriminator + ' was unbanned')
                await channel.send('**user ' + str(user) + ' was unbanned**')

    #Clearing Messages
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, context, amount=5):
        print(str(context.author) + ' cleared ' +  str(amount) + ' messages')
        await context.channel.purge(limit = amount + 1)

def setup(client):
    client.add_cog(moderation(client))
