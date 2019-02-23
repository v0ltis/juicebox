import discord
from discord.ext.commands import Bot
from discord.ext import commands
import youtube_dl
from itertools import cycle
import asyncio
import time
import os
import random

import scrapy

from my_directory import dir_location
import text_to_url

client = commands.Bot(command_prefix = '/')

merde = ["MERDE","CHIER","CHIANT","CHIE"]
chat_filter = ["PUTE","SALOPE","CONNARD","CUL","ABRUTIT","NIQUE","ENCULE","CHATTE","BITE","CON","BITCH","PUTIN","FOUTRE","ASS","TRISO","GOGOL","COQUIN","BATARDE","FELATION","SEX","VTFF","NTM"]
bypass_list = ["362615539773997056","528268989525131274","402896241429577729","281134477877575680"]
ban_user = ["159985870458322944"]
memeaudio = ["https://www.youtube.com/watch?v=ma7TL8jJT0A",
	     "https://www.youtube.com/watch?v=5aFP-iR7hPg",
	     "https://www.youtube.com/watch?v=rrvFFjoqg8A",
	     "https://www.youtube.com/watch?v=QglFGVDcuX8",
	     "https://www.youtube.com/watch?v=XE6YaLtctcI",
	     "https://www.youtube.com/watch?v=caXgpo5Ezo4",
	     "https://www.youtube.com/watch?v=6IG4aHDFBYw",
	     "https://www.youtube.com/watch?v=1IySOpdDCx0",
	     "https://www.youtube.com/watch?v=Q5LZcw6MASA",
	     "https://www.youtube.com/watch?v=o6RQuIbzwJk",
	     "https://www.youtube.com/watch?v=H07zYvkNYL8",
	     "https://www.youtube.com/watch?v=Ygnez_odlNg"]

nb_of_serv_where_i_am_connected = 0


@client.event
async def on_ready():
	a = dir_location()
	a.search()
	a.got_tot_file('sonds_fonction.py')
	b = open(a.me,'r')
	c = b.read()
	b.close()
	exec(c)
	
	global nb_of_serv_where_i_am_connected
	print("Logged in as:", client.user.name)
	print("ID:", client.user.id)

	#channel_dem = discord.utils.get(message.server.channels, name = 'serveurs-juicebox-x-delete')

	#await client.delete_channel(channel_dem)
	await client.send_message(discord.Object(id='543490625773895681'), 'Redemarage effectué !')
	#await client.create_channel("JuiceBox Support", "serveurs-juicebox-x-delete")
	#await client.send_message(channel_dem, "Les serveurs auquel je suis connecté sont :\n")
	for x in client.servers:
		nb_of_serv_where_i_am_connected += 1
		print(nb_of_serv_where_i_am_connected,x.name + x.owner.name)
		#nb_server_juicy = await client.send_message(channel_dem,str(nb_of_serv_where_i_am_connected))
		#serveur_juicy = await client.send_message(channel_dem, x.name + x.owner)
	await client.change_presence(game=discord.Game(name='/help - ' + nb_of_serv_where_i_am_connected + ' serveurs'))
	
players = {}
queues = {}
chat_on = False
play_on = False
play_on_patched = {}
player = None


@client.event
async def on_message(message):
	global chat_on
	if message.author.id in ban_user:
			return
	if message.author == client.user:
			return

	if message.content.upper().startswith("/CHAT ON"):
		chat_on = True
	if message.content.upper().startswith("/CHAT OFF"):
		chat_on = False

	if chat_on == True:
		chat = "Serveur du message : {}, channel du message : {}, message : {}".format(message.server.name,message.channel.name,message.content)
		print(chat)
		await client.send_message(discord.Object(id='547516410343981057'), chat)

	if message.content.upper().startswith("/PING"):
		timePing = time.monotonic()
		pinger = await client.send_message(message.channel, ":ping_pong: **Pong !**")
		ping = "%.2f"%(1000* (time.monotonic() - timePing))
		await client.edit_message(pinger, ":ping_pong: **Pong !**\n\
`Ping:" + ping + "`")
				
	if message.content.upper().startswith("/SAY"):
		args = message.content.split(" ")
		await client.send_message(message.channel, (" ".join(args[1:])))
				 
			
			
	if message.content.upper().startswith("/TICKET"):
		args = message.content.split(" ")
		await client.send_message(message.channel, "Votre ticket a bien été envoyé au staff , merci !")
		ticket=discord.Embed(color=0x7a2581)
		ticket.set_author(name="JuiceBox", icon_url="https://juicebot.github.io/assets/images/juicebox-112x112.png")
		ticket.add_field(name="Utilisateur", value=message.author, inline=False)
		ticket.add_field(name="Tiket :", value=(" ".join(args[1:])), inline=False)
		ticket.set_footer(text="ID de l'utilisateur : " + message.author.id) 
		await client.send_message(discord.Object(id="544830498099298324"), embed=ticket)
		await client.send_message(message.author, "Merci de nous avoir contacté, un membre du staff va vous repondre au plus vite !")
				 
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
			"https://tenor.com/yiQN.gif",
			"https://tenor.com/view/cobie-smulders-sad-crying-wine-upset-gif-3550883",
			"https://tenor.com/view/ted-teddy-bear-bear-hump-humping-gif-4762693",
			"https://tenor.com/view/shocked-omg-australiasgottalent-noway-gif-5027549",
			"https://tenor.com/view/cat-neutered-kitten-what-wtf-gif-10638247",
			"https://gph.is/2SGx6It",
			"https://media.giphy.com/media/l4FGpPki5v2Bcd6Ss/giphy.gif",
			"https://thumbs.gfycat.com/NaiveMatureArmedcrab-small.gif"]))
		
		message_content = message.content.split(' ')[1]
		print(message_content)

	if message.content.upper().startswith("/HELP"):
		help = discord.Embed(title='Commandes:', description='Voici la liste des commandes', colour=0x7a2581)
		help.set_author(name='Juicebox', icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
		help.add_field(name="Prefix:", value="/", inline=False)
		help.add_field(name="/fun", value="Donne les commandes de fun", inline=True)
		help.add_field(name="/moderation", value="Donne les commandes de moderations", inline=True)
		help.add_field(name="/musique", value="Donne les commandes de musique", inline=True)
		help.add_field(name="/support", value="Donne les commandes en liens avec mes devlopeurs !", inline=True) 
		help.set_footer(text=message.author)
		await client.send_message(message.channel, embed=help)
		
		
	if message.content.upper().startswith("/SUPPORT"):
		dev = discord.Embed(title='Commandes de support:', description='Voici la liste des commandes pour vous aider a meiux connaitre Juicy !', colour=0x7a2581)
		dev.add_field(name="/ticket", value="Envoie un message aux devlopeurs", inline=True)
		dev.add_field(name="/site", value="Donne le lien de note site: ``https://juicebot.github.io``.", inline=True)
		dev.add_field(name="/discord", value="Donne notre serveur du support: ``https://discord.gg/Abfvn9y``.", inline=True)
		dev.set_footer(text=message.author)
		await client.send_message(message.channel, embed=dev)
	
	
	if message.content.upper().startswith("/MUSIQUE"):
		musique = discord.Embed(title='Commandes musicales:', description='Voici la liste des commandes de la musique:', colour=0x7a2581)
		musique.set_author(name='Juicebox', icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
		musique.add_field(name=" /join", value="Fait rejoindre juicebox dans votre salon vocal ", inline=True)
		musique.add_field(name="/play", value=" lis la video/musique (l'URL doit être un URL YouTube) ", inline=True)
		musique.add_field(name=" /stop", value="Arette la video", inline=True)
		musique.add_field(name="/pause", value="Met en pause la video", inline=True)
		musique.add_field(name="/resume", value="Reprend la video", inline=True)
		musique.add_field(name="/leave", value="Fait quitter juiceBox de votre salon vocal", inline=True)
		musique.set_footer(text=message.author)
		await client.send_message(message.channel, embed=musique)
	
	if message.content.upper().startswith("/FUN"):
		fun = discord.Embed(title="Commandes fun", description="Voici les commandes fun:", colour=0x7a2581)
		fun.set_author(name="JuiceBox", icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
		fun.add_field(name="/say + texte", value="Fait dire au bot le texte", inline=True)
		fun.add_field(name="/gif", value="Donne un gif aléatoire", inline=True)
		fun.add_field(name="/memeaudio ***Bientot...***", value="???", inline=True)
		fun.set_footer(text=message.author)
		await client.send_message(message.channel, embed=fun)
	
	if message.content.upper().startswith("/MODERATION"):
		modo = discord.Embed(title="Commandes de modération:", description="Voici la liste des commandes de moderations:", colour=0x7a2581)
		modo.set_author(name="JuiceBox", icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
		modo.add_field(name="/report", value="Signale les méchant utilisateur dans #report ! \n Fonctionement : /report (mention) (raison)", inline=True)
		modo.add_field(name="Gros-mots", value="Je suprimme automatiquement les insultes !", inline=True)
		modo.set_footer(text=message.author)
		await client.send_message(message.channel, embed=modo)
		
	if message.content.upper().startswith("/REPORT"):
		args = message.content.split(" ")
		arg_1 = ("".join(args[1]))
		arg_2 = (" ".join(args[2:]))
				
		report=discord.Embed(color=0x700127)
		report.set_author(name="JuiceBox", icon_url="https://juicebot.github.io/assets/images/juicebox-112x112.png")
		report.add_field(name="Utilisateur signalé:", value=arg_1, inline=False)
		report.add_field(name="Signalé par", value=message.author, inline=False)
		report.add_field(name="Signalé pour la raison suivante :", value=arg_2, inline=False)
		channel = discord.utils.get(message.server.channels, name = 'report')
		try:
			await client.send_message(channel, embed=report)
			await client.send_message(message.author, "Votre signalement a bien été envoyé")
		except:
			await client.send_message(message.channel, "Erreur ... voici les choses a faire :\nVerifier que le salon report existe bien.\nVerifier que vous avez bien donné une raison au report.\n Ca ne marche toujour pas ? Evoyez nous un ticket !")
					
					
	if (message.channel.name == "youtube"):
		await client.add_reaction(message, "<:youtube:314349922885566475>")
		
	if message.content.upper().startswith("/MEMEAUDIO"):
		await meme_audio(message)

	if message.content.upper().startswith("/DISCORD"):
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
		await client.send_message(message.channel,"Bonjour , je suis JuiceBox , voici quelques commandes qui pourait vous aider : \n /help : affiche l'aide \n /musique : affiche les commandes de musique ")      

	for word in contents:
		if word.upper() in merde:
			await client.delete_message(message)
			await client.send_message(message.channel, ":shit:")
							
						
	if message.content.upper().startswith("YO"):
		if not message.content.upper().startswith("YOU"):
			await client.send_message(message.channel,random.choice(["ga","plait"]))

	if message.content.upper().startswith("/TEST"):
		await a_test_fonction(message)


	if message.content.upper().startswith("BONJOUR"):
		await client.send_message(message.channel,"Hey!")

	if message.content.upper().startswith("GG"):
		await client.send_message(message.channel,":clap: :clap: :clap:") 

	if message.content.upper().startswith("/BOTADMIN"):
		await client.delete_message(message)
		await client.send_message(message.channel,"Hey Boss , code here: https://github.com/v0ltis/juicebox/edit/master/index.py")
		
	if message.content.upper().startswith("/INFO"):
		rien = ""
		if len(message.mentions) > 0:
			for user in message.mentions:
				info_mention=discord.Embed(color=0x700127)
				info_mention.set_author(name="JuiceBox", icon_url="https://juicebot.github.io/assets/images/juicebox-112x112.png")
				info_mention.set_thumbnail(url=user.avatar_url)
				info_mention.add_field(name="Voici les informations de " + user.name +" :",value="", inline=False)
				info_mention.add_field(name="Pseudo / ID", value=user.name + " / " + user.id, inline=False)
				info_mention.add_field(name="Sur ce serveur depuis:", value=user.joined_at, inline=False)
				info_mention.add_field(name="Date de création du compte:", value=user.created_at, inline=False)
				info_mention.add_field(name="Avec les roles:", value=user.roles, inline=False)
				await client.send_message(message.channel, embed=info_mention)
				
		else:
			info=discord.Embed(color=0x700127)
			info.set_author(name="JuiceBox", icon_url="https://juicebot.github.io/assets/images/juicebox-112x112.png")
			info.set_thumbnail(url=message.author.avatar_url)
			info.add_field(name="Voici les informations de " + message.author.name +" :", inline=False)
			info.add_field(name="Pseudo / ID", value=message.author.name + " / " + message.author.id, inline=False)
			info.add_field(name="Sur ce serveur depuis:", value=message.author.joined_at, inline=False)
			info.add_field(name="Date de création du compte:", value=message.author.created_at, inline=False)
			info.add_field(name="Avec les roles:", value=message.author.roles, inline=False)
			await client.send_message(message.channel, embed=info)
		
	#join
	if message.content.upper().startswith("/JOIN"):
		await join(message)

	#play + query
	if message.content.upper().startswith("/PLAY"):
		await play(message)

	#pause
	if message.content.upper().startswith("/PAUSE"):
		await pause(message)
	
	#resume
	if message.content.upper().startswith("/RESUME"):
		await resume(message)

	#STOP
	if message.content.upper().startswith("/STOP"):
		await stop(message)

	#leave
	if message.content.upper().startswith("/LEAVE"):
		await leave(message)

	if message.content.upper().startswith("/QUEUE"):
		await queue(message)

client.run(os.environ['TOKEN_BOT'])
