import discord
import youtube_dl
from discord.ext.commands import Bot
from discord.ext import commands
from itertools import cycle
import asyncio
import time
import os

client = commands.Bot(command_prefix = '/')

merde = ["MERDE","CHIER"]
chat_filter = ["PUTE","SALOPE","CONNARD","CUL","ABRUTIT","NIQUE","ENCULE","CHATTE","BITE","CON","BITCH","PUTIN","FOUTRE","ASS","TRISO","GOGOL","COQUIN","BATARDE","FELATION","SEX","VTFF","NTM"]
bypass_list = ["362615539773997056","437289213616979968"]


status = ['/help', '/musique', 'JuiceBox V.1.5']
async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(5)


@client.event
async def on_ready():
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
    
    
    if message.content.upper().startswith("<@528268989525131274>"):
       await client.send_message(message.channel,"Bonjour , je suis JuiceBox , voicis quelques commandes qui pourait vous aider : \n /help : affiche l'aide \n /musique : affiche les commandes de musique : \n /ping : affiche le ping ")      
    
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
    

    #play + url
    if message.content.upper().startswith("/PLAY"):
      print(message.content)
      message_url = message.content
      url = message_url.split(" ")[1]
      if len(message_url.split(" ")) == 1:
        message_channel = message.channel
        message_content = "Je vais avoir besoin d'un url !"
        await client.send_message(message_channel,message_content)
      if len(message_url.split(" ")) == 2:
        print(url)
        server = message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        try:
          player.start()
        except:
          message_channel = message.channel
          message_content = "Buuuuuuuuuuug ... ça ne viens pas forcement de moi , essayez avec un autre URL YouTube. \n Url: " + str(url)
          await client.send_message(message_channel,message_content)
        message_channel = message.channel

        print("Let's play : " + str(url))
        message_content = "C'est parti pour : " + str(url)
        await client.send_message(message_channel,message_content)
      if len(message_url.split(" ")) == 3:
        message_channel = message.channel
        message_content = "Heu ... je peut avoir un URL s'il vous plait ?"
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
