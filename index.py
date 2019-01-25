import discord
import youtube_dl
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

import text_to_url

client = commands.Bot(command_prefix = '/')

merde = ["MERDE"]
chat_filter = ["PUTE","SALOPE","CONNARD","CUL","ABRUTIT","NIQUE","ENCULE","CHATTE","BITE","CON","BITCH","PUTIN","FOUTRE","ASS","TRISO","GOGOL","COQUIN","BATARDE","FELATION","SEX","VTFF","NTM"]
bypass_list = ["362615539773997056","437289213616979968"]

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="/help"))
    print("Logged in as:", client.user.name)
    print("ID:", client.user.id)
    
    
players = {}

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
        help = discord.Embed(title='Commandes:', description='Voici la liste des commandes', colour=0x7a2581)
        help.set_author(name='Juicebox', icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
        help.add_field(name="Prefix:", value="/", inline=False)
        help.add_field(name="/help", value="Affiche les commandes", inline=True)
        help.add_field(name="/say (+texte)", value="Fait dire au bot le texte", inline=True)
        help.add_field(name="/ping", value="Affiche le ping", inline=True)
        help.add_field(name="/musique", value="donne les commandes musicales du bot", inline=False)
        await client.send_message(message.channel, embed=help)
                   
    if message.content.upper().startswith("/MUSIQUE"):
        musique = discord.Embed(title='Commandes musicales:', description='Voici la liste des commandes de la musique', colour=0x7a2581)
        musique.set_author(name='Juicebox', icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
        musique.add_field(name=" /join :", value="Fait rejoindre juicebox dans votre salon vocal ", inline=True)
        musique.add_field(name="/play (+URL) :", value=" lis la video/musique (l'URL doit être un URL YouTube) ", inline=True)
        musique.add_field(name=" /stop", value="Arette la video", inline=True)
        musique.add_field(name="/pause", value="Met en pause la video", inline=True)
        musique.add_field(name="/resume", value="Reprend la video", inline=True)
        musique.add_field(name="/leave", value="Fait quitter juiceBox de votre salon vocal", inline=True)
        await client.send_message(message.channel, embed=musique)
        
       
    if message.content.upper().startswith("XD"):
       await client.send_message(message.channel,"lol")

    if message.content.startswith("🖕"):
       await client.send_message(message.channel,":rage:")

    for word in contents:
           if word.upper() in merde:
                await client.delete_message(message)
                await client.send_message(message.channel, ":shit:")
                
    if message.content.upper().startswith("YO"):
       await client.send_message(message.channel,"plait")

    if message.content.upper().startswith("BONJOUR"):
       await client.send_message(message.channel,"Hey!")

    if message.content.upper().startswith("GG"):
       await client.send_message(message.channel,":clap: :clap: :clap:") 

    if message.content.upper().startswith("/BOTADMIN"):
        await client.delete_message(message)
        await client.send_message(message.channel,"Hey Boss , code here: https://github.com/v0ltis/juicebox/edit/master/index.py")
    
    

    #join
    if message.content.upper().startswith("/JOIN"):
        channel = message.author.voice.voice_channel
        print("I'm connected to : " + str(channel))
        await client.join_voice_channel(channel)

    #play + query
    if message.content.upper().startswith("/PLAY"):
      print(message.content)
      message_url = message.content
      url = message_url.split(" ")[1]
      if len(message_url.split(" ")) == 1:
        message_channel = message.channel
        message_content = "Je vais avoir besoin d'un url ou d'un !"
        await client.send_message(message_channel,message_content)
      if len(message_url.split(" ")) >= 2:
        debug = 0
        for x in message_url.split("."):
          if x == 'youtube':
            debug += 1
          if x == 'com':
            debug += 1
          if x == 'watch':
            debug += 1
        if debug >= 3:
          print(url)
          print("I'm taking the first way !")
          server = message.server
          voice_client = client.voice_client_in(server)
          player = await voice_client.create_ytdl_player(url)
          players[server.id] = player

          try:
            player.start()
            message_channel = message.channel
            print("Let's play : " + str(url))
            message_content = "C'est parti pour : " + str(url)
            await client.send_message(message_channel,message_content)

          except:
            message_channel = message.channel
            message_content = "Buuuuuuuuuuug ... ça ne viens pas forcement de moi , essayez avec un autre URL YouTube. \n Url: " + str(url)
            await client.send_message(message_channel,message_content)

        else:
          print("I'm taking the second way !")
          msg_query = message.content.split(' ')
          msg_query.pop(0)

          msg_query_end = ''
          x=0

          for x in range(len(msg_query)-1):
            msg_query_end = msg_query_end + msg_query[x] + ' '

          msg_query_t = msg_query_end + msg_query[x+1]
          print(msg_query_t)
          url =text_to_url.url_find('yt_url_spider.py','quotes.json','https://www.youtube.com',str(msg_query_t)).get_complete_url()
          print(url)
          server = message.server
          voice_client = client.voice_client_in(server)
          player = await voice_client.create_ytdl_player(url)
          players[server.id] = player

          try:
            player.start()
            message_channel = message.channel
            print("Let's play : " + str(url))
            message_content = "C'est parti pour : " + str(url)
            await client.send_message(message_channel,message_content)

          except:
            message_channel = message.channel
            message_content = "Buuuuuuuuuuug ... ça ne viens pas forcement de moi , essayez avec un autre URL YouTube. \n Url: " + str(url)
            await client.send_message(message_channel,message_content)

    #pause
    if message.content.upper().startswith("/PAUSE"):
      id = message.server.id
      players[id].pause()
      message_channel = message.channel
      message_content = "Pause :+1:"
      await client.send_message(message_channel,message_content)

    
    #resume
    if message.content.upper().startswith("/RESUME"):
      id = message.server.id
      players[id].resume()
      message_channel = message.channel
      message_content = "Je recomence"
      await client.send_message(message_channel,message_content)


    #STOP
    if message.content.upper().startswith("/STOP"):
      id = message.server.id
      players[id].stop()
      message_channel = message.channel
      message_content = "Ok , ok , j'arrete"
      await client.send_message(message_channel,message_content)


    #leave
    if message.content.upper().startswith("/LEAVE"):
      server = message.server
      print("I'm disconnected from : " + str(server))
      voice_client = client.voice_client_in(server)
      try:
        for x in range(0,100):
          await voice_client.disconnect()
      except:
        print("Error ...")
        message_channel = message.channel
        message_content = "Buuuuuug... attend un peut ou essaye avec /join'."
        await client.send_message(message_channel,message_content)

client.run(os.environ['TOKEN_BOT'])
