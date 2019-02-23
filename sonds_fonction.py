#Be carefull this document can't be used alone you need index.py for some varioables

async def send_msg(channel,content):
	message_channel = channel
	message_content = str(content)
	await client.send_message(message_channel,message_content)
	
	
async def join_meme(message):
	global play_on
	play_on = False
	try:
		channel = message.author.voice.voice_channel
		print("I'm connected to : " + str(channel))
		await client.join_voice_channel(channel)
	except:
		pass
#await send_msg(message.channel,"Erreur ...(join command)")

async def join(message):
	global play_on
	play_on = False
	try:
		channel = message.author.voice.voice_channel
		print("I'm connected to : " + str(channel))
		await client.join_voice_channel(channel)
		await client.send_message(message.channel, "Je suis pret à chanter !")
		await client.send_message(discord.Object(id='543490625773895681'), 'Je me suis connecté  à \n ID:' + channel.id +'\n Nom du channel : "***' + channel.name + '"***' \
			+'\n Nom du serveur : "***' + message.server.name + '"***')
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

async def play_url(message,url):
	global player,play_on

	await join(message)

	if player != None:
		if player.is_done() == False:
			print("Je n'ai pas fini ! : " + str(url))
			await send_msg(message.channel,"Laisse moi finir s'il te plait")
			return
	
	server = message.server
	voice_client = client.voice_client_in(server)
	player = await voice_client.create_ytdl_player(url)
	players[server.id] = player
	print(player,players)
	try:
		if player.is_done() == True or play_on == False:
			time.sleep(5)
			player.start()
			print("Let's play : " + str(url))
			await send_msg(message.channel,("C'est parti pour : " + str(url)))
			play_on = True

		else:
			print("Je n'ai pas fini ! : " + str(url))
			await send_msg(message.channel,"Laisse moi finir s'il te plait")

	except:
		await send_msg(message.channel,("Buuuuuuuuuuug ... ça ne viens pas forcement de moi , essayez avec un autre URL YouTube. \n Url: " + str(url)))

async def play_url_meme(message,url):
	global player,play_on

	await join(message)

	if player != None:
		if player.is_done() == False:
			print("Je n'ai pas fini ! : " + str(url))
			await send_msg(message.channel,"Laisse moi finir s'il te plait")
			return
	
	server = message.server
	voice_client = client.voice_client_in(server)
	player = await voice_client.create_ytdl_player(url)
	players[server.id] = player
	print(player,players)
	try:
		if player.is_done() == True or play_on == False:
			time.sleep(5)
			player.start()
			print("Go pour: " + str(url))
			await send_msg(message.channel,("C'est parti !"))
			play_on = True

		else:
			print("Je n'ai pas fini !")
			await send_msg(message.channel,"Laisse moi finir s'il te plait")

	except:
		await send_msg(message.channel,("Buuuuuuuuuuug ... ça ne viens pas forcement de moi , essayez plus tard , ou prevenez mes devlopeurs avec /ticket."))
		
		
		
async def play(message):
	global play_on,player
	
	message_url = message.content
	url = message_url.split(" ")[1]
	print(url)
	
	https = await verifie_url(message)
	if https == True:
		print("Https == True")
		await join(message)

		await play_url(message,url)

	elif https == False:
		print("Https == False")
		await join(message)
			
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
		
		try:
			url =text_to_url.url_find('yt_url_spider_v2.py','https://www.youtube.com',str(msg_query_end)).get_complete_url()
			print(url)
		
		except:
			await client.send_message(message.channel,"Erreur ... Essaye avec un autre url.")

		await play_url(message,url)

def test(message):
	emji = client.wait_for_reaction()
	print(emji)
	for x in emji:
		yield x

async def meme_audio(message):
	await join_meme(message)

	url = random.choice(memeaudio)
	try:
		if message.content.split(' ')[1] != None:
			msg = await client.send_message(message.channel,"Voulez-vous jouer un meme audio ?")
			await msg.add_reaction(emoji='✅')
			print(emji)

			print(test(message)+'\n')

			await client.add_reaction(msg,emji)
			'''
			msg = await client.wait_for_message(author=None)
			print(msg.author)
			
			try:
				print(message)
			
			except:
				pass
			
			print(msg)

			print("I'm waiting for reaction : False")
			react_test = await client.wait_for_reaction()

			await message.add_reaction(msg,discord.Emoji(name=":white_check_mark:"))

			print("I'm waiting for reaction : False")
			react_test = await client.wait_for_reaction()
			await client.send_message(message.channel,str(react_test))

			react = await client.wait_for_reaction(message=msg,emoji=':white_check_mark:')
			'''
			await client.send_message(message.channel,str(react))

	except:
		pass

	await play_url_meme(message,url)

	while True:
		if player.is_done() == True:
			time.sleep(5)
			await leave(message)
			break

async def queue(message):
	pass

async def a_test_fonction(msg):
	print(msg.content)
	await client.send_message(msg.channel,str(msg.content)) 