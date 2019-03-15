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

import my_directory
import text_to_url

client = commands.Bot(command_prefix = '/')
prefix = '/'


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
	     "https://www.youtube.com/watch?v=Ygnez_odlNg",
	     "https://www.youtube.com/watch?v=wPqo_q-HgmE",
	     "https://www.youtube.com/watch?v=8vgQCArK2sY",
	     "https://www.youtube.com/watch?v=xAdo9bgToTk",
	     "https://www.youtube.com/watch?v=Pr8ETbGz35Q",
	     "https://www.youtube.com/watch?v=0gx7z2ohiZQ"]


news_emb = "Mise a jour 1.8 : \n Ajout du ***__/memeaudio__*** : Joue un meme dans votre salon vocal! \n Ajout d'un ***__/info__*** : Apprenez tout sur les membres de votre serveur ... ou vous même! \n Nouvautée: Juicebox affiche désormais le nombre de serveurs sur lequel il est connecté ! c'est pas super ?"    

nb_of_serv_where_i_am_connected = 0

admin = ['TheLicheIsBack','v0ltis']

boucle = False

async def boucle():
	global boucle
	global nb_of_serv_where_i_am_connected
	boucle == True
	await client.change_presence(game=discord.Game(name=serv_co))
	time.sleep(15)
	await client.change_presence(game=discord.Game(name="/help"))
	time.sleep(15)
	await client.change_presence(game=discord.Game(name="juicebot.github.io"))
	time.sleep(15)

	for x in client.servers:
		nb_of_serv_where_i_am_connected += 1
		serv_co = str(nb_of_serv_where_i_am_connected) + 'serveurs'

	await client.change_presence(game=discord.Game(name=("/help "+serv_co)))

	boucle = False

@client.event
async def on_ready():
	global nb_of_serv_where_i_am_connected
	print("Logged in as:", client.user.name)
	print("ID:", client.user.id)
	nb_of_serv_where_i_am_connected = 0
	for x in client.servers:
		nb_of_serv_where_i_am_connected += 1
		serv_co = str(nb_of_serv_where_i_am_connected) + 'serveurs'

	nb_of_serv_where_i_am_connected = 0
	
	for x in client.servers:
		nb_of_serv_where_i_am_connected += 1
		serv_co = str(nb_of_serv_where_i_am_connected) + ' serveurs'

	await client.send_message(discord.Object(id='543490625773895681'), 'Redemarage effectué !')
	
	await client.change_presence(game=discord.Game(name=("/help "+serv_co)))

	#upload l'emoji juicebot sur tout les serveurs
	juiceboxemoji = False
	for x in client.servers:
		for y in x.emojis:
			if y.name == "JuiceBox":
				#already this emoji
				juiceboxemoji = True
		if juiceboxemoji == False:
			await client.create_custom_emoji(x,name='JuiceBox',image=open('JuiceBot.png','rb').read())
		else:
			juiceboxemoji = False
			
players = {}
queues = {}
chat_on = False
player = None
filename = {}
temps_zero = 0
'''
forme du type:
{
	message.server.id : nomdufichier à jouer
}

'''
play_on = {}#True si le player et en train de jouer et False s'il ne joue pas | forme : message.server.id : True/False

#dev commands

async def dev_command(message):
	url = message.content.split(' ')[1]
	try:
		channel = message.author.voice.voice_channel
		print("I'm connected to : " + str(channel))
		await client.join_voice_channel(channel)
	except:
		pass

	server = message.server
	voice_client = client.voice_client_in(server)
	'''
	with youtube_dl.YoutubeDL({'format':'bestaudio/best'}) as ydl:
    	ydl.download([])
    '''
	print(os.getcwd())
	with youtube_dl.YoutubeDL({'format':'bestaudio/best'}) as ydl:
		filename = ydl.prepare_filename(ydl.extract_info(url))
		ydl.download([url])

	player = voice_client.create_ffmpeg_player(filename)
	players[server.id] = player
	player.start()


#Messages fonctions

async def send_msg(channel,content):
	message_channel = channel
	message_content = str(content)
	await client.send_message(message_channel,message_content)


#Information fonction

async def info(message):
	info_mention_user = None
	
	if message.mentions != []:
		info_mention_user = message.mentions[0]
	else:
		info_mention_user = message.author

	info_mention=discord.Embed(color=0x700127)
	info_mention.set_author(name="JuiceBox", icon_url="https://juicebot.github.io/assets/images/juicebox-112x112.png")
	info_mention.set_thumbnail(url=info_mention_user.avatar_url)
	info_mention.add_field(name="Voici les informations de :",value=info_mention_user, inline=False)
	info_mention.add_field(name="Pseudo / ID", value=info_mention_user.name + " / " + info_mention_user.id, inline=False)
	info_mention.add_field(name="Sur ce serveur depuis:", value=info_mention_user.joined_at, inline=False)
	info_mention.add_field(name="Date de création du compte:", value=info_mention_user.created_at, inline=False)

	list_user_roles = []

	for x in info_mention_user.roles:
		list_user_roles.append(x.name)
	list_user_roles = str(list_user_roles)

	info_mention.add_field(name="Avec les roles:", value=list_user_roles, inline=False)
	
	info_mention.set_footer(text=message.author)

	

	await client.send_message(message.channel, embed=info_mention)


#Music fonctions

async def join(message,comment=False):
	global play_on
	try:
		if client.is_voice_connected(message.server):
			pass
		else:
			channel = message.author.voice.voice_channel
			print("I'm connected to : " + str(channel))
			await client.join_voice_channel(channel)
			if comment == True:
				await client.send_message(message.channel, "Je suis pret à chanter !")
				await client.send_message(discord.Object(id='543490625773895681'), 'Je me suis connecté  à \n ID:' + channel.id +'\n Nom du channel : "***' + channel.name + '"***' \
					+'\n Nom du serveur : "***' + message.server.name + '"***')
			await stop()
			play_on[message.server.id] = False

	except:
		pass
		#await send_msg(message.channel,"Erreur ...(join command)")

async def leave(message):
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

async def pause(message):
	id = message.server.id
	players[id].pause()
	message_channel = message.channel
	message_content = "Pause :+1:"
	await client.send_message(message_channel,message_content)

async def resume(message):
	id = message.server.id
	players[id].resume()
	message_channel = message.channel
	message_content = "Je recomence"
	await client.send_message(message_channel,message_content)

async def stop(message):
	id = message.server.id
	players[id].stop()
	message_channel = message.channel
	message_content = "Ok , ok , j'arrete"
	await client.send_message(message_channel,message_content)

async def verif_play(message):
	print(message.content)
	message_url = message.content
	url = message_url.split(" ")[1]

	if len(message_url.split(" ")) == 1:
		await send_msg(message.content,"Je vais avoir besoin d'un url")

	if len(message_url.split(" ")) >= 2:
		pass

#renvoie True si il s'agit d'un url sinon False
async def verifie_url(message):
	message_url = message.content
	url = message_url.split(" ")[1]
	if len(message_url.split(" ")) == 1:
		await send_msg(message.content,"Je vais avoir besoin d'un url")

	if len(message_url.split(" ")) >= 2:
		debug = 0
		print(message_url.split("://")[0].split(' '))
	
		if message_url.split("://")[0].split(' ')[1] == 'https':
			debug += 1
			print(url)
			print("Https detecté !")
			return True
		else:
			return False

async def play_url(message,url,comment=False):
	global player,ytdl_format_options

	await join(message,comment)

	server = message.server
	voice_client = client.voice_client_in(server)

	with youtube_dl.YoutubeDL({'format':'bestaudio/best'}) as ydl:
		filename[server.id] = ydl.prepare_filename(ydl.extract_info(url))
		ydl.download([url])

	player = voice_client.create_ffmpeg_player(filename[server.id])
	players[server.id] = player
#try:
	if play_on.get(server.id) == None:
		play_on[server.id] == False

	#verifier que le bot ne joue pas déjà une musique pour empecher un crash
	if players[server.id].is_done() == True or play_on[server.id] == False:
		play_on[server.id] = True
		player.start()
		print("Let's play : " + str(url))
		
		if comment != False:
			await send_msg(message.channel,("C'est parti pour : " + str(url)))
		
		#action à la fin de lecture
		while not players[server.id].is_done():
			pass
		play_on[server.id] = False
		time.sleep(1)
		await leave(message)

	else:
		print("Je n'ai pas fini ! : " + str(url))
		await send_msg(message.channel,"Laisse moi finir s'il te plait")
'''
	except ExceptionType, Argument:
		await send_msg(message.channel,("Buuuuuuuuuuug ... ça ne viens pas forcement de moi , essayez avec un autre URL YouTube ou attendez un peu. \n Url: " + str(url) +'\n\t```{} : ```'.format(str(ExceptionType),str(Argument))))
'''	

async def play(message):
	global player
	
	message_url = message.content
	url = message_url.split(" ")[1]
	print(url)
	
	https = await verifie_url(message)
	if https == True:
		print("Https == True")
		await play_url(message,url,True)

	elif https == False:
		print("Https == False")
			
		msg_query = message.content.split(' ')
		msg_query.pop(0)

		msg_query_end = ''
		x=0

		for x in range(len(msg_query)-1):
			msg_query_end = msg_query_end + msg_query[x] + ' '
						
		try:
			msg_query_end = msg_query_end + msg_query[x+1]

		except:
			pass
			
		print(msg_query_end)
		
		url =text_to_url.url_find('yt_url_spider_v2.py','https://www.youtube.com',str(msg_query_end)).get_complete_url()
		print(url)


		await play_url(message,url,True)

#antispam
async def agreement(message):
	msg = await client.send_message(message.channel,"Veux tu jouer un meme audio aléatoire ? (clique sur ok)")
	await client.add_reaction(msg,emoji='✅')

	def check(reaction, user):
		return True
	
	time.sleep(2)
	res = await client.wait_for_reaction(emoji='✅',message=msg, check=check)

	while str(res.user).split('#')[0] != str(message.author.name):
		time.sleep(1)
		res = await client.wait_for_reaction(emoji='✅',message=msg, check=check)

	return True

async def break_until_agrement_is_true(message):
	turn = 0
	while True:
		agr = await agreement(message=message)
		if agr == True:
			return True
		if turn == 20:
			return False
		turn += 1
		time.sleep(1)



def arg_meme_audio(message):
	pass#url,titre

async def meme_audio(message):
	if message.content.endswith('-l'):
		msg_meme_audio = []

		for x in memeaudio:
			msg_meme_audio.append(await client.send_message(message.channel,x))

		time.sleep(10)

		for x in msg_meme_audio:
			await client.delete_message(x)
	else:
		await join(message,False)

		url = random.choice(memeaudio)
		await play_url(message,url,False)

		while True:
			if player.is_done() == True:
				time.sleep(5)
				await leave(message)
				break

async def queue(message):
	pass

async def verifie_admin(message):
	global admin
	
	for x in admin:
		if message.author.name == x:
			await client.send_message(message.channel,'You are {}, proceed ...'.format(message.author.name))
			return True

	await client.send_message(message.channel,'You are not an admin.')
	return False

async def close(message):
	if await verifie_admin(message) == True:
		await client.close()

@client.event
async def on_message(message):
	global chat_on,temps_zero,boucle
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
		help.add_field(name="/musique ***BUGS***", value="Donne les commandes de musique", inline=True)
		help.add_field(name="/support", value="Donne les commandes en liens avec mes devlopeurs !", inline=True)
		help.add_field(name="/news", value="Ok JuiceBox , quelles sont les dernières nouveautées ?", inline=False)
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
		musique.add_field(name="/play ***BUGS***", value=" lis la video/musique (l'URL doit être un URL YouTube) ", inline=True)
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
		fun.add_field(name="/memeaudio ***(Nouveau)***", value="Joue un meme (audio) dans votre salon vocal !", inline=True)
		fun.add_field(name="/info + *mention [optionel]* ***(nouveau)***", value="Donne toutes les informations sur les membres du serveur... ou vous-même!", inline=True)
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
			await client.add_reaction(message.channel,emoji='💩')
							
						
	if message.content.upper().startswith("YO"):
		if not message.content.upper().startswith("YOU"):
			await client.send_message(message.channel,random.choice(["ga","plait"]))

	if message.content.upper().startswith("BONJOUR"):
		await client.send_message(message.channel,"Hey!")

	if message.content.upper().startswith("GG"):
		await client.send_message(message.channel,":clap: :clap: :clap:") 

	if message.content.upper().startswith("/BOTADMIN"):
		await client.delete_message(message)
		await client.send_message(message.channel,"Hey Boss , code here: https://github.com/v0ltis/juicebox/edit/master/index.py")
	
	if message.content.upper().startswith("/NEWS"):
		news=discord.Embed(color=0x700127)
		news.set_author(name="JuiceBox", icon_url="https://juicebot.github.io/assets/images/juicebox-112x112.png")
		news.add_field(name="Dernière nouveautées :", value=news_emb, inline=False)
		await client.send_message(message.author, embed=news)
	
	if message.content.upper().startswith("/INFO"):
		await info(message)
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
	if message.content.upper().startswith(prefix + "LEAVE"):
		await leave(message)

	if message.content.upper().startswith(prefix + "QUEUE"):
		await queue(message)

	if message.content.upper().startswith(prefix + "CLOSE"):
		await close(message)

	if message.content.upper().startswith(prefix + "DEV_COMMAND"):
		await dev_command(message)

	if temps_zero - time.time() >= 5 and boucle == False:
		await boucle()
	else:
		temps_zero == time.time()

client.run(os.environ['TOKEN_BOT'])
