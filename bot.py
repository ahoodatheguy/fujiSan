# packages
import discord #discord library
from discord.ext import commands #commands

prefix = "!" #command prefix

#Client
client = commands.Bot(command_prefix="!") #the discord bot, also sets a prefix as !

# EVENTS

# Execute this code block when bot connects to server
@client.event
async def on_ready(): 
    print("Bot is running!")

@client.event
async def on_disconnect():
    print("bot has disconnected")


#aboutme command
@client.command(name="aboutme") #run run if prefix + "aboutme" is sent
async def aboutme(context): #the 'context' or arguments after the command is sent. function name MUST be the same as context
    print("bot info was requested")
    aboutEmbed = discord.Embed(title="Fuji-San", description="A work in progress discord bot.", color=0x00ff00) #basic embed structure. color is self explanatory. make sure to use hexadecimal code.
    aboutEmbed.add_field(name="Github: ", value="https://www.github.com/ahoodatheguy", inline=False)
    aboutEmbed.add_field(name="Version:", value="Beta v1.0.0", inline=False)
    aboutEmbed.set_author(name="ahoodatheguy", url="https://twitter.com/freeahooda", icon_url="https://pbs.twimg.com/profile_images/1369100469075853314/cjg-yHFL_400x400.jpg")
    aboutEmbed.set_footer(text="ありがとう")
    channel = context.message.channel #assigns the channel where the message is sent to variable channel
    await channel.send(embed=aboutEmbed) #send embed
#credits command
@client.command(name="credits")
async def credits(context): #run when command credits is sent
        print("Credits were requested")
        channel = context.message.channel # get the channel the command was sent in
        await channel.send("Created by Ahooda")
        await channel.send("Check out his github here: https://www.github.com/ahoodatheguy")
        
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
# Connect to server and run bot
client.run("YOUR TOKEN HERE")
