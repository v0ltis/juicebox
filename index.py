import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

client = discord.Client()
chat_filter = ["PUTE","SALOPE","CONNARD","CUL","ABRUTIT","NIQUE","ENCULE","CHATTE","BITE","CON"]
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
      embed=discord.Embed(title="Help:", description="Commandes :\n**~Help:**  affiche les commandes\n**~Say** (+text): dit le text\n**~Ping** : affiche le ping\n- - - - - - - - - - - - - - - - - - -\nL**iens** :\n[Chaine YouTube de Silvathor](https://www.youtube.com/channel/UCe_nGFDs5_r1hRbL5l3JcfQ)\n[Inviter des personnes sur notre serveur discord](https://discord.me/https://discord.me/minecraft_tips")
embed.set_author(name="Juice Box", icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
await client_send(embed=embed)
             

            
client.run(os.environ['TOKEN_BOT'])


