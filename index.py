import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

client = discord.Client()
chat_filter = ["PUTE","SALOPE","CONNARD","CUL","ABRUTIT","NIQUE","ENCULE","CHATTE","BITE","CON","BITCH","PUTIN","FOUTRE","ASS","TRISO","GOGOL","COQUIN","BATARDE","FELATION","SEX","VTFF","NTM"]
bypass_list = ["362615539773997056","437289213616979968"]

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="/help"))
    print("Logged in as:", client.user.name)
    print("ID:", client.user.id)

@client.event
async def on_message(message):    
    if message.content.upper().startswith("/PING"):
      timePing = time.monotonic()
      pinger = await client.send_message(message.channel, ":ping_pong: **Pong !**")
      ping = "%.2f"%(1000* (time.monotonic() - timePing))
      await client.edit_message(pinger, ":ping_pong: **Pong !**\n\
`Ping:" + ping + "`")
        
    if message.content.upper().startswith("/SAY"):
          args = message.content.split(" ")
          await client.send_message(message.channel, (" ".join(args[1:])))
    contents = message.content.split(" ")
    for word in contents:
           if word.upper() in chat_filter:
             if not message.author.id in bypass_list:
                await client.delete_message(message)
                await client.send_message(message.channel, "**Hey!** un peut de respect!!!")
   
    if message.content.upper().startswith("/HELP"):
    embed = discord.Embed(title="Help:", description="Voici les commandes            ", color=0x630c52)
    embed.set_author(name="JuiceBox",, icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
    embed.add_field(name=Préfix :, value=/, inline=False)
    embed.add_field(name=/help, value=affiche les commandes, inline=True)
    embed.add_field(name=/say (+texte), value=dit le texte, inline=True)
    embed.add_field(name=/ping, value=affiche le ping, inline=True)
    embed.set_footer(text="commande help")
    await self.bot.say(embed=embed)
    if message.content.upper().startswith("XD"):
            await client.send_message(message.channel,"lol")

    if message.content.startswith("🖕"):
            await client.send_message(message.channel,":rage:")

    if message.content.upper().startswith("MERDE"):
            await client.delete_message(message)
            await client.send_message(message.channel,":shit:")

    if message.content.upper().startswith("YO"):
            await client.send_message(message.channel,"plait")

    if message.content.upper().startswith("BONJOUR"):
            await client.send_message(message.channel,"Hey!")

    if message.content.upper().startswith("GG"):
            await client.send_message(message.channel,":clap: :clap: :clap:")

            
client.run(os.environ['TOKEN_BOT'])
