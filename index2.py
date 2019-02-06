import discord
import youtube_dl
from discord.ext.commands import Bot
from discord.ext import commands
from itertools import cycle
import asyncio
import time
import os
import random

import scrapy

import my_directory
import text_to_url

client = commands.Bot(command_prefix = '/')

merde = ["MERDE","CHIER","CHIANT"]
chat_filter = ["PUTE","SALOPE","CONNARD","CUL","ABRUTIT","NIQUE","ENCULE","CHATTE","BITE","CON","BITCH","PUTIN","FOUTRE","ASS","TRISO","GOGOL","COQUIN","BATARDE","FELATION","SEX","VTFF","NTM"]
bypass_list = ["362615539773997056","437289213616979968","528268989525131274","402896241429577729"]

def check_queue(id):
  if queues[id] != []:
    player = queues[id].pop(0)
    players[id] = player
    player.start()

@client.event
async def on_ready():
    print("Logged in as:", client.user.name)
    print("ID:", client.user.id)
    await client.change_presence(game=discord.Game(name='/help-https://juicebot.github.io'))

    
    
players = {}
queues = {}


@client.event
async def on_message(message):   
    if message.author == client.user:
        return

  
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
                
    if message.content.upper().startswith("/GIF"):
        await client.send_message(message.channel, random.choice(["https://giphy.com/gifs/AuIvUrZpzBl04",
                                                                  "https://giphy.com/gifs/hello-hey-big-brother-l0MYBbEvqqi1kfuyA",
                                                                  "https://giphy.com/gifs/wow-amazing-l4FGETcwLzIZ1IaGs",
                                                                  "https://giphy.com/gifs/trump-donald-eclipse-xUNen16DFqlM6v6DEQ",
                                                                  "https://tenor.com/view/ok-okay-gif-5307535",
                                                                  "https://gph.is/2iUaL8y",
                                                                  "https://gph.is/19aLnvI",
                                                                  "https://gph.is/2fiQFj1",
                                                                  "https://gph.is/1rr0eCj",
                                                                  "https://media.giphy.com/media/joPQLwo2kbXe8/giphy.gif",
                                                                  "https://media.giphy.com/media/QGzPdYCcBbbZm/giphy.gif",
                                                                  "https://media.giphy.com/media/w1XrYq5PsCbyE/giphy.gif",
                                                                  "https://gph.is/2tBvKBE",
                                                                  "https://tenor.com/view/smile-golden-retriever-break-neck-gif-7733809",
                                                                  "https://tenor.com/view/pinguino-furbo-frozen-excited-gif-13388703",
                                                                  "https://gph.is/2lnp32Z",
                                                                  "https://gph.is/2rwmnmy",
                                                                  "https://tenor.com/4iLj.gif",
                                                                  "https://tenor.com/4gdR.gif",
                                                                  "https://tenor.com/yFDW.gif",
                                                                  "https://tenor.com/4n8e.gif",
                                                                  "https://tenor.com/yiQN.gif"]))
        message_content = message.content.split(' ')[1]
        print(message_content)


    if message.content.upper().startswith("/HELP"):
        help = discord.Embed(title='Commandes:', description='Voici la liste des commandes', colour=0x7a2581)
        help.set_author(name='Juicebox', icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
        help.add_field(name="Prefix:", value="/", inline=False)
        help.add_field(name="/help", value="Affiche les commandes", inline=True)
        help.add_field(name="/say (+texte)", value="Fait dire au bot le texte", inline=True)
        help.add_field(name="/ping", value="Affiche le ping", inline=True)
        help.add_field(name="/gif ***(BETA)***", value="Donne un GIF aleatoirement!", inline=True)
        help.add_field(name="/musique", value="donne les commandes musicales du bot", inline=False)
        help.add_field(name="/site", value="Donne le lien de note site: ``https://juicebot.github.io``.", inline=True)
        help.add_field(name="/support", value="Donne notre serveur du support: ``https://discord.gg/Abfvn9y``.", inline=True)
        await client.send_message(message.channel, embed=help)
                   
    if message.content.upper().startswith("/MUSIQUE"):
        musique = discord.Embed(title='Commandes musicales:', description='Voici la liste des commandes de la musique', colour=0x7a2581)
        musique.set_author(name='Juicebox', icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
        musique.add_field(name=" /join :", value="Fait rejoindre juicebox dans votre salon vocal ", inline=True)
        musique.add_field(name="/play:", value=" lis la video/musique (l'URL doit être un URL YouTube) ", inline=True)
        musique.add_field(name=" /stop", value="Arette la video", inline=True)
        musique.add_field(name="/pause", value="Met en pause la video", inline=True)
        musique.add_field(name="/resume", value="Reprend la video", inline=True)
        musique.add_field(name="/leave", value="Fait quitter juiceBox de votre salon vocal", inline=True)
        await client.send_message(message.channel, embed=musique)
        
    if message.content.upper().startswith("/SUPPORT"):
      await client.send_message(message.channel,"Venez papoter ici: \n https://discord.gg/Abfvn9y")
      
    if message.content.upper().startswith("/SITE"):
      await client.send_message(message.channel,"Ma maison c'est ici: \n https://juicebot.github.io/")
        
       
    if message.content.upper().startswith("XD"):
       await client.send_message(message.channel,random.choice(["lol",
                                                                " ",
                                                                " "]))

    if message.content.startswith("🖕"):
       await client.send_message(message.channel,":rage:")
    
    
    if message.content.upper().startswith("<@528268989525131274>"):
       await client.send_message(message.channel,"Bonjour , je suis JuiceBox , voicis quelques commandes qui pourait vous aider : \n /help : affiche l'aide \n /musique : affiche les commandes de musique : \n /ping : affiche le ping ")      
    
    for word in contents:
           if word.upper() in merde:
                await client.delete_message(message)
                await client.send_message(message.channel, ":shit:")
              
              
    if message.content.upper().startswith("/LOCATE _VOLTIS"):
       if message.channel.id == ("459444059556020228"):
        await client.send_message("voltis est dans ton cul !")
       else:
        return
                
    if message.content.upper().startswith("YO"):
       if message.content.upper().startswith("YOU"):
          return
       else:
        await client.send_message(message.channel,random.choice(["ga",
                                                                "plait"]))

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
        message_content = "Je vais avoir besoin d'un url"
        await client.send_message(message_channel,message_content)
      if len(message_url.split(" ")) >= 2:
        debug = 0

        print(message_url.split("://")[0].split(' '))
        if message_url.split("://")[0].split(' ')[1] == 'https':
          debug += 1
          
        if debug >= 1:
          print(url)
          print("I'm taking the first way !")
          try:
            channel = message.author.voice.voice_channel
            print("I'm connected to : " + str(channel))
            await client.join_voice_channel(channel)
          except:
            pass
          server = message.server
          voice_client = client.voice_client_in(server)
          player = await voice_client.create_ytdl_player(url,after=lambda: check_queue(server.id))
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

          try:
            channel = message.author.voice.voice_channel
            print("I'm connected to : " + str(channel))
            await client.join_voice_channel(channel)
          except:
            pass

          msg_query = message.content.split(' ')
          msg_query.pop(0)

          msg_query_end = ''
          x=0

          for x in range(len(msg_query)-1):
            msg_query_end = msg_query_end + msg_query[x] + ' '
            
          msg_query_end = msg_query_end + msg_query[x+1]
          print(msg_query_end)
          url =text_to_url.url_find('yt_url_spider_v2.py','https://www.youtube.com',str(msg_query_end)).get_complete_url()
          print(url)
          server = message.server
          voice_client = client.voice_client_in(server)
          player = await voice_client.create_ytdl_player(url,after=lambda: check_queue(server.id))
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
    
    #queue + query
    if message.content.upper().startswith("/QUEUE"):
      print(message.content)
      message_url = message.content
      url = message_url.split(" ")[1]
      if len(message_url.split(" ")) == 1:
        message_channel = message.channel
        message_content = "Je vais avoir besoin d'un url"
        await client.send_message(message_channel,message_content)
      if len(message_url.split(" ")) >= 2:
        debug = 0

        print(message_url.split("://")[0].split(' '))
        if message_url.split("://")[0].split(' ')[1] == 'https':
          debug += 1
          
        if debug >= 1:
          print(url)
          print("I'm taking the first way !")
          try:
            channel = message.author.voice.voice_channel
            print("I'm connected to : " + str(channel))
            await client.join_voice_channel(channel)
          except:
            pass
          server = message.server
          voice_client = client.voice_client_in(server)
          player = await voice_client.create_ytdl_player(url,after=lambda: check_queue(server.id))
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

          try:
            channel = message.author.voice.voice_channel
            print("I'm connected to : " + str(channel))
            await client.join_voice_channel(channel)
          except:
            pass

          msg_query = message.content.split(' ')
          msg_query.pop(0)

          msg_query_end = ''
          x=0

          for x in range(len(msg_query)-1):
            msg_query_end = msg_query_end + msg_query[x] + ' '
            
          msg_query_end = msg_query_end + msg_query[x+1]
          print(msg_query_end)
          url =text_to_url.url_find('yt_url_spider_v2.py','https://www.youtube.com',str(msg_query_end)).get_complete_url()
          print(url)
          server = message.server
          voice_client = client.voice_client_in(server)
          player = await voice_client.create_ytdl_player(url,after=lambda: check_queue(server.id))
          players[server.id] = player

          if server.id in queues:
            queues[server.id].append(player)
          else:
            queues[server.id] = [player]
          await client.say('Video queued.')

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
    
    if message.content.upper().startswith("/QUEUE"):
      print(message.content)
      message_url = message.content
      url = message_url.split(" ")[1]
        
'''
async def queue(ctx,url):
  server = message.server
  voice_client = client.voice_client_in(server)
  player = await voice_client.create_ytdl_player(url,after=lambda: check_queue(server.id))

  if server.id in queues:
    queues[server.id].append(player)
  else:
    queues[server.id] = [player]
  await client.say('Video queued.')
'''
client.run(os.environ['TOKEN_BOT'])
