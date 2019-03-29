import discord
from discord.ext.commands import Bot
from discord.ext import commands
import youtube_dl
from itertools import cycle
import asyncio
import time
import os
import random

import my_directory
import text_to_url

#Constantes
from constant_class import Juice_constants
Const = Juice_constants()

client = Const.client
prefix = Const.prefix

from class_play_on import ready
@client.event
async def on_ready():
	await ready(client).ready()


chat_on = False

numbers = ['-1','-2','-3','-4','-5','-6','-7','-8','-9','-10','-0']
ingnored_serv = ["264445053596991498","110373943822540800"]

def react_with_numbers(message):
	nmbrs = []
	print("React with numbers fonction" + str(message.content.split(' ')))
	for x in message.content.split(' '):
		if x in numbers:
			e = numbers.index(x)
			nmbrs.append(e)

	if nmbrs != []:
		for x in range(0,len(nmbrs)):
			if nmbrs.count(x) > 1:
				a = nmbrs
				a.reverse()
				a.remove(nmbrs[x])
				a.reverse()
				nmbrs = a
		return (True,nmbrs)
	return (False,None)


#Information fonction
from class_add_on import plug_in#currently nothing here
from class_add_on import info#info fonc
from class_add_on import verifie_admin
from class_add_on import clear

#Music fonctions
from music_foncts import Music_bot

mBot = Music_bot(client,Const.memeaudio)	

@client.event
async def on_message(message):
	global chat_on,temps_zero,boucle
	if message.author.id in Const.ban_user:
			return
	elif message.author == client.user:
			return

	elif message.content.upper().startswith("/CHAT ON"):
		chat_on = True
	elif message.content.upper().startswith("/CHAT OFF"):
		chat_on = False

	elif chat_on == True:
		chat = "Serveur du message : {}, channel du message : {}, message : {}".format(message.server.name,message.channel.name,message.content)
		print(chat)
		await client.send_message(discord.Object(id='547516410343981057'), chat)

	elif message.content.upper().startswith("/PING"):
		timePing = time.monotonic()
		pinger = await client.send_message(message.channel, ":ping_pong: **Pong !**")
		ping = "%.2f"%(1000* (time.monotonic() - timePing))
		await client.edit_message(pinger, ":ping_pong: **Pong !**\n\
`Ping:" + ping + "`")
				
	elif message.content.upper().startswith("/SAY"):
		args = message.content.split(" ")
		await client.send_message(message.channel, (" ".join(args[1:])))
				 
			
			
	elif message.content.upper().startswith("/TICKET"):
		args = message.content.split(" ")
		await client.send_message(message.channel, "Votre ticket a bien été envoyé au staff , merci !")
		ticket=discord.Embed(color=0x7a2581)
		ticket.set_author(name="JuiceBox", icon_url="https://juicebot.github.io/assets/images/juicebox-112x112.png")
		ticket.add_field(name="Utilisateur", value=message.author, inline=False)
		ticket.add_field(name="Tiket :", value=(" ".join(args[1:])), inline=False)
		ticket.set_footer(text="ID de l'utilisateur : " + message.author.id) 
		await client.send_message(discord.Object(id="544830498099298324"), embed=ticket)
		await client.send_message(message.author, "Merci de nous avoir contacté, un membre du staff va vous repondre au plus vite !")
								
	elif message.content.upper().startswith("/GIF"):
		await client.send_message(message.channel, random.choice(Const.gifs))
		
		message_content = message.content.split(' ')[1]
		print(message_content)
		
	
	elif message.content.upper().startswith("/HELP"):
		help = discord.Embed(title='Commandes:', description='Voici la liste des commandes', colour=0x7a2581)
		help.set_author(name='Juicebox', icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
		help.add_field(name="Prefix:", value="/", inline=False)
		help.add_field(name="/fun", value="Donne les commandes de fun", inline=True)
		help.add_field(name="/moderation", value="Donne les commandes de moderations", inline=True)
		help.add_field(name="/musique", value="Donne les commandes de musique", inline=True)
		help.add_field(name="/support", value="Donne les commandes en liens avec mes devlopeurs !", inline=True)
		help.add_field(name="/news", value="Ok JuiceBox , quelles sont les dernières nouveautées ?", inline=False)
		help.set_footer(text=message.author)
		await client.send_message(message.channel, embed=help)
		
		
	elif message.content.upper().startswith("/SUPPORT"):
		dev = discord.Embed(title='Commandes de support:', description='Voici la liste des commandes pour vous aider a meiux connaitre Juicy !', colour=0x7a2581)
		dev.add_field(name="/ticket", value="Envoie un message aux devlopeurs", inline=True)
		dev.add_field(name="/site", value="Donne le lien de note site: ``https://juicebot.github.io``.", inline=True)
		dev.add_field(name="/discord", value="Donne notre serveur du support: ``https://discord.gg/Abfvn9y``.", inline=True)
		dev.set_footer(text=message.author)
		await client.send_message(message.channel, embed=dev)
	
	
	elif message.content.upper().startswith("/MUSIQUE"):
		musique = discord.Embed(title='Commandes musicales:', description='Voici la liste des commandes de la musique:', colour=0x7a2581)
		musique.set_author(name='Juicebox', icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
		musique.add_field(name=" /join", value="Fait rejoindre juicebox dans votre salon vocal ", inline=True)
		musique.add_field(name="/play + url/recherche", value=" lis la video/musique (l'URL doit être un URL YouTube) (si il ne s'agit pas d'un url, la recherche sera automatiquement effectuée sur YouTube) ", inline=True)
		musique.add_field(name=" /stop", value="Arette la video", inline=True)
		musique.add_field(name="/pause", value="Met en pause la video", inline=True)
		musique.add_field(name="/resume", value="Reprend la video", inline=True)
		musique.add_field(name="/leave", value="Fait quitter juiceBox de votre salon vocal", inline=True)
		musique.set_footer(text=message.author)
		await client.send_message(message.channel, embed=musique)
	
	elif message.content.upper().startswith("/FUN"):
		fun = discord.Embed(title="Commandes fun", description="Voici les commandes fun:", colour=0x7a2581)
		fun.set_author(name="JuiceBox", icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
		fun.add_field(name="/say + texte", value="Fait dire au bot le texte", inline=True)
		fun.add_field(name="/gif", value="Donne un gif aléatoire", inline=True)
		fun.add_field(name="/memeaudio ***(Nouveau)***", value="Joue un meme (audio) dans votre salon vocal !", inline=True)
		fun.add_field(name="/info + *mention [optionel]* ***(nouveau)***", value="Donne toutes les informations sur les membres du serveur... ou vous-même!", inline=True)
		fun.set_footer(text=message.author)
		await client.send_message(message.channel, embed=fun)
	
	elif message.content.upper().startswith("/MODERATION"):
		modo = discord.Embed(title="Commandes de modération:", description="Voici la liste des commandes de moderations:", colour=0x7a2581)
		modo.set_author(name="JuiceBox", icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
		modo.add_field(name="/report", value="Signale les méchants utilisateurs dans #report ! \n Fonctionement : /report (mention) (raison)", inline=True)
		modo.add_field(name="Gros-mots", value="Je supprime automatiquement les insultes !", inline=True)
		modo.set_footer(text=message.author)
		await client.send_message(message.channel, embed=modo)
		
	elif message.content.upper().startswith("/REPORT"):
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
			await client.send_message(message.channel, "Erreur ... voici les choses à faire :\nVerifier que le salon report existe bien.\nVerifier que vous avez bien donné une raison au report.\n Ca ne marche toujour pas ? Evoyez nous un ticket !")
					

		
	elif message.content.upper().startswith(Const.prefix + "MEMEAUDIO"):
		print("Memeaudioing.")
		await mBot.meme_audio(message)

	elif message.content.upper().startswith("/DISCORD"):
		await client.send_message(message.channel,"Venez papoter ici: \n https://discord.gg/Abfvn9y")
			
	elif message.content.upper().startswith("/SITE"):
		await client.send_message(message.channel,"Ma maison c'est ici: \n https://juicebot.github.io/")
				
			 
	elif message.content.upper().startswith("XD"):
		await client.send_message(message.channel,random.choice(["lol",
			" ",
			" "]))

	elif message.content.startswith("🖕"):
		await client.send_message(message.channel,":rage:")
		
	elif message.content.upper().startswith("<@528268989525131274>"):
		await client.send_message(message.channel,"Bonjour , je suis JuiceBox , voici quelques commandes qui pouraient vous aider : \n /help : affiche l'aide \n /musique : affiche les commandes de musique ")

	elif message.content.upper().startswith("/REACT"):
		args = message.content.split(" ")
		emoji_arg = args[1]
		try:
			await client.add_reaction(message,emoji=emoji_arg)
		except:
			await client.send_message(message.channel,"Je n'ai pas trouvé d'emoji ``" + str(emoji_arg) +"`` . Ou aors vous ne savez pas ce qu'est un emoji ...")
						
	elif message.content.upper().startswith("YO"):
		if not message.content.upper().startswith("YOU"):
			await client.send_message(message.channel,random.choice(["ga","plait"]))

	elif message.content.upper().startswith("BONJOUR"):
		await client.send_message(message.channel,"Hey!")

	elif message.content.upper().startswith("GG"):
		await client.send_message(message.channel,":clap: :clap: :clap:") 

	elif message.content.upper().startswith("/BOTADMIN"):
		await client.delete_message(message)
		await client.send_message(message.channel,"Hey Boss , code here: https://github.com/v0ltis/juicebox/edit/master/index.py")
	
	elif message.content.upper().startswith(Const.prefix + "NEWS"):
		news=discord.Embed(color=0x700127)
		news.set_author(name="JuiceBox", icon_url="https://juicebot.github.io/assets/images/juicebox-112x112.png")
		news.add_field(name="Dernières nouveautées :", value=Const.news_emb, inline=False)
		await client.send_message(message.author, embed=news)
	
	elif message.content.upper().startswith(Const.prefix + "INFO"):
		await info(client,message)
	#join
	elif message.content.upper().startswith(Const.prefix + "JOIN"):
		await mBot.join(message)

	#play + query
	elif message.content.upper().startswith(Const.prefix + "PLAY"):
		print("Playing.")
		await mBot.play(message)

	#pause
	elif message.content.upper().startswith(Const.prefix + "PAUSE"):
		await mBot.pause(message)
	
	#resume
	elif message.content.upper().startswith(Const.prefix + "RESUME"):
		await mBot.resume(message)

	#STOP
	elif message.content.upper().startswith(Const.prefix + "STOP"):
		await mBot.stop(message)

	#leave
	elif message.content.upper().startswith(Const.prefix + "LEAVE"):
		await mBot.leave(message)

	elif message.content.upper().startswith(Const.prefix + "QUEUE"):
		await queue(message)

	elif message.content.upper().startswith(Const.prefix + "CLOSE"):
		await close(client,message)

	elif message.content.upper().startswith(Const.prefix + "CLEAR"):
		amount = message.content.split(' ')[1]
		await clear(client,message,amount=amount)

	elif react_with_numbers(message)[0]:
			react_nb = react_with_numbers(message)
			if not message.channel.id.upper in ingnored_serv:
				nb = react_nb[1]
				msg_reactions = await client.get_message(discord.Object('545336065955987492'),'560172166046416940')
				reactions = msg_reactions.reactions
				for x in nb:
					await client.add_reaction(message,reactions[x].emoji)#r[0] = :one: , r[1] = :two: , r[9] = 10, r[10] = 0

	contents = message.content.split(" ")
	for word in contents:
		if word.upper() in Const.chat_filter:
			if not message.author.id in Const.bypass_list:
				await client.delete_message(message)
				await client.send_message(message.channel, "**Hey!** un peut de respect!!!")
	
	for word in contents:
		if word.upper() in Const.merde:
			await client.add_reaction(message,emoji='💩')


client.run(os.environ["TOKEN_BOT"])
