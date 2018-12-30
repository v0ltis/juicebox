import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

client = discord.Client()
chat_filter = ["PUTE","SALOPE","CONNARD","CUL","ABRUTIT","NIQUE","ENCULE","CHATTE","BITE","CON","BITCH","PUTIN","FOUTRE","ASS","TRISO","GOGOL","COQUIN","BATARDE","FELATION","SEX"]
bypass_list = ["362615539773997056","437289213616979968"]

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="~help"))
    print("Logged in as:", client.user.name)
    print("ID:", client.user.id)

@client.event
async def on_message(message):    
    if message.content.upper().startswith("~PING"):
      timePing = time.monotonic()
      pinger = await client.send_message(message.channel, ":ping_pong: **Pong !**")
      ping = "%.2f"%(1000* (time.monotonic() - timePing))
      await client.edit_message(pinger, ":ping_pong: **Pong !**\n\
`Ping:" + ping + "`")
        
    if message.content.upper().startswith("~SAY"):
          args = message.content.split(" ")
          await client.send_message(message.channel, (" ".join(args[1:])))
    contents = message.content.split(" ")
    for word in contents:
           if word.upper() in chat_filter:
             if not message.author.id in bypass_list:
                await client.delete_message(message)
                await client.send_message(message.channel, "**Hey!** un peut de respect!!!")
   
    if message.content.upper().startswith("~HELP"):
      await client.send_message(message.channel, "__**Préfix :**__ ~ \n __**Commandes:**__ \n __~help__ : Affiche les commandes \n __~say__*(+text)*: dit le text \n__~ping__: affiche le ping") 

            
client.run(os.environ['TOKEN_BOT'])


