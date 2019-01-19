import discord
import youtube_dl
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

client = commands.Bot(command_prefix = '/')


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
              
   #AUTO-REPLY HERE !!!
    if message.content.upper().startswith("/HELP"):
        help = discord.Embed(title='Commandes:', description='Voici la liste des commandes', colour=0x7a2581)
        help.set_author(name='Juicebox', icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
        help.add_field(name="Prefix:", value="/", inline=False)
        help.add_field(name="/help", value="Affiche les commandes", inline=True)
        help.add_field(name="/say (+texte)", value="Fait dire au bot le texte", inline=True)
        help.add_field(name="/ping", value="Affiche le ping", inline=True)
        await client.send_message(message.channel, embed=help)
        
        
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

    if message.content.upper().startswith("/BOTADMIN"):
        await client.delete_message(message)
        await client.send_message(message.channel,"Hey Boss , code here: https://github.com/v0ltis/juicebox/edit/master/index.py")
    
    

    #join
  @bot.command(pass_context=True)
async def skip(con):
    if con.message.channel.is_private == True:
        await bot.send_message(con.message.channel, "**You must be in a `server text channel` to use this command**")

    # COMMAND NOT IN DM
    if con.message.channel.is_private == False:
        if servers_songs[con.message.server.id] == None or len(song_names[con.message.server.id]) == 0 or player_status[con.message.server.id] == False:
            await bot.send_message(con.message.channel, "**No songs in queue to skip**")
        if servers_songs[con.message.server.id] != None:
            bot.loop.create_task(queue_songs(con, True, False))

@bot.command(pass_context=True)
async def join(con,*,channel=None):
    """JOIN A VOICE CHANNEL THAT THE USR IS IN OR MOVE TO A VOICE CHANNEL IF THE BOT IS ALREADY IN A VOICE CHANNEL"""


    # COMMAND IS IN DM
    if con.message.channel.is_private == True:
        await bot.send_message(con.message.channel, "**You must be in a `server text channel` to use this command**")

    # COMMAND NOT IN DM
    if con.message.channel.is_private == False:
        voice_status = bot.is_voice_connected(con.message.server)

        voice=find(lambda m:m.name == channel,con.message.server.channels)

        if voice_status == False and channel == None:  # VOICE NOT CONNECTED
            if con.message.author.voice_channel == None:
                await bot.send_message(con.message.channel,"**You must be in a voice channel or give a voice channel name to join**")
            if con.message.author.voice_channel != None:
                await bot.join_voice_channel(con.message.author.voice.voice_channel)

        if voice_status == False and channel != None:  # PICKING A VOICE CHANNEL
            await bot.join_voice_channel(voice)

        if voice_status == True:  # VOICE ALREADY CONNECTED
            if voice == None:
                await bot.send_message(con.message.channel, "**Bot is already connected to a voice channel**")


            if voice != None:            
                if voice.type == discord.ChannelType.voice:
                     await bot.voice_client_in(con.message.server).move_to(voice)


@bot.command(pass_context=True)
async def leave(con):
    """LEAVE THE VOICE CHANNEL AND STOP ALL SONGS AND CLEAR QUEUE"""
    # COMMAND USED IN DM
    if con.message.channel.is_private == True:
        await bot.send_message(con.message.channel, "**You must be in a `server text channel` to use this command**")

    # COMMAND NOT IN DM
    if con.message.channel.is_private == False:

        # IF VOICE IS NOT CONNECTED
        if bot.is_voice_connected(con.message.server) == False:
            await bot.send_message(con.message.channel, "**Bot is not connected to a voice channel**")

        # VOICE ALREADY CONNECTED
        if bot.is_voice_connected(con.message.server) == True:
            bot.loop.create_task(queue_songs(con, False, True))

@bot.command(pass_context=True)
async def pause(con):
    # COMMAND IS IN DM
    if con.message.channel.is_private == True:
        await bot.send_message(con.message.channel, "**You must be in a `server text channel` to use this command**")

    # COMMAND NOT IN DM
    if con.message.channel.is_private == False:
        if servers_songs[con.message.server.id] != None:
            if paused[con.message.server.id] == True:
                await bot.send_message(con.message.channel, "**Audio already paused**")
            if paused[con.message.server.id] == False:
                servers_songs[con.message.server.id].pause()
                paused[con.message.server.id] = True





@bot.command(pass_context=True)
async def resume(con):
    # COMMAND IS IN DM
    if con.message.channel.is_private == True:
        await bot.send_message(con.message.channel, "**You must be in a `server voice channel` to use this command**")

    # COMMAND NOT IN DM
    if con.message.channel.is_private == False:
        if servers_songs[con.message.server.id] != None:
            if paused[con.message.server.id] == False:
                await bot.send_message(con.message.channel, "**Audio already playing**")
            if paused[con.message.server.id] == True:
                servers_songs[con.message.server.id].resume()
                paused[con.message.server.id] = False



@bot.command(pass_context=True)
async def volume(con,vol:float):
    if player_status[con.message.server.id] == False:
        await bot.send_message(con.message.channel,"No Audio playing at the moment")
    if player_status[con.message.server.id] == True:
        servers_songs[con.message.server.id].volume =vol;


client.run(os.environ['TOKEN_BOT'])
