import discord
import youtube_dl
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

client = discord.Client()
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
       
@client.command(pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	txtch = ctx.message.channel
	print("I'm connected to : " + str(channel))
	await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def play(ctx,url):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = await voice_client.create_ytdl_player(url)
	players[server.id] = player
	try:
		player.start()
	except:
		message_channel = ctx.message.channel
		message_content = "Error ... It can be an author error.Try with another youtube url.Url : \n" + str(url)
		await client.send_message(message_channel,message_content)
	message_channel = ctx.message.channel
	print("Let's play : " + str(url))
	message_content = "Let's play : " + str(url)
	await client.send_message(message_channel,message_content)

@client.command(pass_context=True)
async def pause(ctx):
	id = ctx.message.server.id
	players[id].pause()
	message_channel = ctx.message.channel
	message_content = "Paused."
	await client.send_message(message_channel,message_content)

@client.command(pass_context=True)
async def resume(ctx):
	id = ctx.message.server.id
	players[id].resume()
	message_channel = ctx.message.channel
	message_content = "Resumed."
	await client.send_message(message_channel,message_content)

@client.command(pass_context=True)
async def stop(ctx):
	id = ctx.message.server.id
	players[id].stop()
	message_channel = ctx.message.channel
	message_content = "Stoped."
	await client.send_message(message_channel,message_content)

@client.command(pass_context=True)
async def leave(ctx):
	server = ctx.message.server
	print("I'm disconnected from : " + str(server))
	voice_client = client.voice_client_in(server)
	try:
		for x in range(0,100):
			await voice_client.disconnect()
	except:
		print("Error ...")
		message_channel = ctx.message.channel
		message_content = ("Error ...Please wait and try again.Or try '//join'.")
                await client.send_message(message_channel,message_content)




client.run(os.environ['TOKEN_BOT'])
