import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

client = discord.Client()
chat_filter = ["PUTE","SALOPE","CONNARD","CUL","ABRUTIT","NIQUE","ENCULE","CHATTE","BITE","CON","BITCH","PUTIN","FOUTRE","ASS","TRISO","GOGOL","COQUIN","BATARDE","FELATION","SEX"]
bypass_list = ["362615539773997056","437289213616979968"]
bot = commands.Bot(command_prefix='~',description='Description')
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="~help"))
    print("Logged in as:", client.user.name)
    print("ID:", client.user.id)

@client.event
async def on_message(message):    
    if message.content.upper().startswith("PING"):
      timePing = time.monotonic()
      pinger = await client.send_message(message.channel, ":ping_pong: **Pong !**")
      ping = "%.2f"%(1000* (time.monotonic() - timePing))
      await client.edit_message(pinger, ":ping_pong: **Pong !**\n\
`Ping:" + ping + "`")
        
    if message.content.upper().startswith("SAY"):
          args = message.content.split(" ")
          await client.send_message(message.channel, (" ".join(args[1:])))
          await bot.delete_message(ctx.message)
    contents = message.content.split(" ")
    for word in contents:
           if word.upper() in chat_filter:
             if not message.author.id in bypass_list:
                await client.delete_message(message)
                await client.send_message(message.channel, "**Hey!** un peut de respect!!!")
   
    @bot.command(pass_context=True)
    async def embed(ctx):
    embed = discord.Embed(name="help", color=0x542765)
    embed.add_field(name"Juice Boxé, value=ctx.message.author.name)
    embed.set_Footer(text="TEST".format(ctx.message.author.name))
    await bot.say(embed=embed)
            
client.run(os.environ['TOKEN_BOT'])




