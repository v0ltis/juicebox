
#needed
from asyncio import *
import time
from discord.ext import commands
import my_directory
import text_to_url
import discord
#Be carefull this document can't be used alone you need index.py for some varioables

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

players = {}
queues = {}
chat_on = False
play_on = False
play_on_patched = {}
player = None

#needed
client = discord.client

async def send_msg(channel,content):
	message_channel = channel
	message_content = str(content)
	await client.send_message(message_channel,message_content)
	
async def join(message,comment=False):
	global play_on
	play_on = False
	try:
		channel = message.author.voice.voice_channel
		print("I'm connected to : " + str(channel))
		await client.join_voice_channel(channel)
		if comment == True:
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

async def verifie_play(message):
	print(message.content)
	message_url = message.content
	url = message_url.split(" ")[1]

	if len(message_url.split(" ")) == 1:
		await send_msg(message.content,"Je vais avoir besoin d'un url")
		return False

	if len(message_url.split(" ")) >= 2:
		return True

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
	global player,play_on

	await join(message,comment)

	if await verifie_play(message) == False:
		return

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
	
async def play(message):
	global play_on,player
	
	message_url = message.content
	url = message_url.split(" ")[1]
	print(url)
	
	https = await verifie_url(message)
	if https == True:
		print("Https == True")
		await join(message,True)

		await play_url(message,url)

	elif https == False:
		print("Https == False")
		await join(message,True)
			
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

async def verif_anti_spam(message,msg_validation="Veux tu jouer un meme audio aléatoire ? (clique sur ok)",emoji='✅'):
	msg = await client.send_message(message.channel,msg_validation)
	await client.add_reaction(msg,emoji=emoji)

	def check(reaction, user):
		return True
	
	time.sleep(2)
	res = await client.wait_for_reaction(emoji=emoji,message=msg, check=check)

	while str(res.user.name) != str(message.author.name):
		time.sleep(1)
		res = await client.wait_for_reaction(emoji=emoji,message=msg, check=check)

	return [True,msg]


async def meme_audio(message):
	await join(message,False)

	url = random.choice(memeaudio)
	anti_spam = 0
	verif_ansp = await verif_anti_spam(message)
	while verif_ansp[0] != True:
		if anti_spam >= 20:
			await client.delete_message()
		time.sleep(1)
		anti_spam += 1

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