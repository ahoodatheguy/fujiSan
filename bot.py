# packages
import discord #discord library
from discord.ext import commands #commands


#Client
client = commands.Bot(command_prefix="!") #the discord bot, also sets a prefix as !

# EVENTS


@client.event
async def on_ready(): #Excecute when bot joins server 
    print("Bot is running!")

@client.event
async def on_disconnect():
    print("bot has disconnected")


#aboutme command
@client.command(name="aboutme") #run run if prefix + "aboutme" is sent
async def aboutme(context):
    print("bot info was requested")
    aboutEmbed = discord.Embed(title="Fuji-San", description="A work in progress discord bot.", color=0x00ff00) #basic embed structure. color is self explanatory. make sure to use hexadecimal code.
    aboutEmbed.add_field(name="Github: ", value="https://www.github.com/ahoodatheguy/fujiSan", inline=False)
    aboutEmbed.add_field(name="Version:", value="Beta v1.0.5", inline=False)
    aboutEmbed.set_author(name="ahoodatheguy", url="https://twitter.com/freeahooda", icon_url="https://pbs.twimg.com/profile_images/1369100469075853314/cjg-yHFL_400x400.jpg")
    aboutEmbed.set_footer(text="ありがとう")
    channel = context.message.channel #assigns the channel where the message is sent to variable channel
    await channel.send(embed=aboutEmbed) #send embed

@client.command(name="socials") 
async def credits(context):
    print("Socials were requested")
    channel = context.message.channel
    socialsEmbed = discord.Embed(title="Social Media", description="You can find me here.", color=0x00ff00)
    #Replace my socials with yours
    socialsEmbed.add_field(name="Twitch:", value="twitch.tv/ahoodatheguy", inline=False)
    socialsEmbed.add_field(name="Twitter:", value="twitter.com/freeahooda", inline=False)
    socialsEmbed.add_field(name="Youtube:", value="youtube.com/channel/UCGcwxAVTRuHmrFrI8cwiC3Q")
    await channel.send(embed=socialsEmbed)

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

 # Connect to server and run bot
client.run("YOUR TOKEN HERE")
