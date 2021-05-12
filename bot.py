# packages
import discord #discord library
from discord.ext import commands #commands


TOKEN = "YOUR TOKEN HERE"
GITHUB = "https://www.github.com/ahoodatheguy/fujiSan"
VERSION = "Beta 1.1.2"
TWITTER = "https://twitter.com/freeahooda"
YOUTUBE = "youtube.com/channel/UCGcwxAVTRuHmrFrI8cwiC3Q"
#Client
client = commands.Bot(command_prefix="!") #the discord bot, also sets prefix
client.remove_command("help") #unbinds the default help command for us to use


@client.event
async def on_ready(): #Excecute when bot joins server
    print("Bot is running!")

VERSION

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
    socialsEmbed.add_field(name="Twitch:", value="twitch.tv/ahoodatheguy", inline=False)
    socialsEmbed.add_field(name="Twitter:", value="twitter.com/freeahooda", inline=False)
    socialsEmbed.add_field(name="Youtube:", value=YOUTUBE)
    await context.reply(embed=socialsEmbed)

@client.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(context,user : discord.Member,*,reason= "reason not given"): #Ban user and tell the chat
    channel = context.message.channel
    await user.ban(reason=reason)
    if reason == "reason not given":
        print("user " + str(user) + " was banned")
        await channel.send(str(user) + " has been banned")
    else:
        await channel.send(str(user) + " has been banned for " + str(reason))
        print("user " + str(user) + " was banned for " + str(reason))

@client.command(name = "vindicate") #unban a user
@commands.has_permissions(ban_members=True)
async def unban(context,*, user):
    channel = context.message.channel
    bannedUsers = await context.guild.bans()
    dName, dDiscriminator = user.split('#')

    for banned in bannedUsers:
        user = banned.user

        if (user.name, user.discriminator) == (dName, dDiscriminator):
            await context.guild.unban(user)
            print(user.name + user.discriminator + " was unbanned")
            await channel.send("user " + str(user) + " was unbanned")
@client.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(context, user : discord.Member,*, reason = "reason not given"):
    channel = context.message.channel
    await user.kick(reason=reason)
    if reason == "reason not given":
        print("user " + str(user) + " was kicked")
        await channel.send(str(user) + " was kicked.")
    else:
        print("user " + str(user) + " was kicked")
        await channel.send(str(user) + " was kicked for " + str(reason))



@client.command(name = "clear")
@commands.has_permissions(manage_messages=True)
async def clear(context, amount=5):
    print(str(context.author) + " cleared " +  str(amount) + " messages")
    await context.channel.purge(limit = amount + 1)

@client.command(name = "help")
async def help(context):

    print("help was requested")
    helpEmbed = discord.Embed(title="Fuji-San commands", description="Commands that you can use in this server", color=0xffb7c5)
    helpEmbed.add_field(name = "help", value = "sends this dialouge", inline = False)
    helpEmbed.add_field(name = "socials", value = "prints socials specified by the moderator", inline = False)
    helpEmbed.add_field(name = "aboutme", value = "get information about the bot and it's creator", inline = False)

    #elif statements werent working.
    if commands.has_permissions(manage_messages = True):
        helpEmbed.add_field(name = "clear <amount>", value = "deletes specified amount of messages (default = 5)", inline = False)
    if commands.has_permissions(ban_members = True):
        helpEmbed.add_field(name = "ban <user>", value = "ban specified user", inline = False)
        helpEmbed.add_field(name = "vindicate <user#12345>", value = "unban specified user", inline = False)
    if commands.has_permissions(kick_members = True):
        helpEmbed.add_field(name = "kick <user>", value = "kick specified user", inline = False)

    await context.reply(embed=helpEmbed)
# Connect to server and run bot
client.run(TOKEN)
