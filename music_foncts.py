import asyncio
import discord
import text_to_url
import os
import youtube_dl
import random

class Music_bot():
	def __init__(self,client,meme_audio_list):
		self.client = client
		self.players = {}
		self.queues = {}
		self.chat_on = False
		self.player = None
		self.filename = {}# {server.id:(fichier, duration, url)}
		self.ytdl_options = {
			'format':'bestaudio/best',
			'default_search': 'auto'
		}
		self.meme_audio_list = meme_audio_list

	async def join(self,message,comment=False):
		print("Joining...")

		for x in range(0,5):
			try:

				if self.client.is_voice_connected(message.server):
					break
				else:
					channel = message.author.voice.voice_channel
					print("I'm connected to : " + str(channel))
					await self.client.join_voice_channel(channel)

					if comment == True:
						await self.client.send_message(message.channel, "Je suis pret à chanter !")
						try:
							await self.client.send_message(discord.Object(id='543490625773895681'), 'Je me suis connecté  à \n ID:' + channel.id +'\n Nom du channel : "***' + channel.name + '"***' \
								+'\n Nom du serveur : "***' + message.server.name + '"***')
						except:
							print("Not allowed.(Join fonction)")
			except:
				pass

	async def leave(self,message):
		print("Leaving")
		server = message.server
		print(server)
		print("I'm disconnected from : " + str(server))
		voice_client = self.client.voice_client_in(server)
		try:
			for x in range(0,100):
				await voice_client.disconnect()
				break

		except:
			print("Error ...")
			await self.client.send_message(message.channel,"Buuuuuug... attend un peu ou essaye avec /join'.")

		while True:
			if server.id in self.filename:
				self.filename[server.id].pop(0)
			else:
				break

	async def pause(self,message):
		id = message.server.id
		players[id].pause()
		message_channel = message.channel
		message_content = "Pause :+1:"
		await self.client.send_message(message_channel,message_content)

	async def resume(self,message):
		id = message.server.id
		players[id].resume()
		message_channel = message.channel
		message_content = "Je recomence"
		await self.client.send_message(message_channel,message_content)
	
	async def stop(self,message):
		id = message.server.id
		players[id].stop()
		message_channel = message.channel
		message_content = "Ok , ok , j'arrete"
		await self.client.send_message(message_channel,message_content)

		while True:
			if server.id in self.filename and queue == False:
				self.filename[server.id].pop(0)
			else:
				break

	async def verif_play(self,message):
		print(message.content)
		message_url = message.content
		url = message_url.split(" ")[1]

		if len(message_url.split(" ")) == 1:
			await self.client.send_message(message.content,"Je vais avoir besoin d'un url")

		if len(message_url.split(" ")) >= 2:
			pass

	async def playlist_loop(self,message,comment,auto_leave=True):
		server = message.server
		voice_client = self.client.voice_client_in(server)
		print(self.filename[server.id])
		self.player = voice_client.create_ffmpeg_player(self.filename[server.id][0][0])
		self.players[server.id] = self.player
		self.player.start()

		print("Let's play : " + str(self.filename[server.id][0][2]))
			
		if comment != False:
			await self.client.send_message(message.channel,("C'est parti pour : " + str(self.filename[server.id][0][2])))
		
		#leave after playing
		print('duration = ' + str(self.filename[server.id][0][1]))
		fmbefore = self.filename[server.id]
		await asyncio.sleep(self.filename[server.id][0][1]+3)
		
		if fmbefore == self.filename[server.id]:
			print("Sleep over !")
			print('Before: ' + str(self.filename[server.id]))
			self.filename[server.id].pop(0)
			print('After: ' + str(self.filename[server.id]))
			if auto_leave:
				await self.leave(message)

	#renvoie True si il s'agit d'un url sinon False
	async def verifie_url(self,message):
		message_url = message.content
		url = message_url.split(" ")[1]
		if len(message_url.split(" ")) == 1:
			await self.client.send_message(message.content,"Je vais avoir besoin d'un url")

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

	async def play_url(self,message,url,comment=False,auto_leave=True,queue=True):
		await self.join(message,comment)

		server = message.server
		voice_client = self.client.voice_client_in(server)
		
		if server.id in self.filename and queue == False:
			await send_msg(message.channel,"Laisse moi finir s'il te plait")
			print("Je n'ai pas finit ! (play_url fonction)")
			return False
		else:
			#if not server.id in filename:
			self.filename[server.id] = []

		output = []
		duration = []
		url_list = []
		#setting output with filename,duration,and dowload the file
		with youtube_dl.YoutubeDL(self.ytdl_options) as ydl:
			output.append(ydl.prepare_filename(ydl.extract_info(url)))
			duration.append(ydl.extract_info(url).get("duration"))
			ydl.download([url])
			url_list.append(url)

		for x in range(len(output)):
			self.filename[server.id].append((output[x],duration[x],url_list[x]))

		await self.playlist_loop(message,comment,auto_leave=auto_leave)

	async def play(self,message):		
		message_url = message.content
		url = message_url.split(" ")[1]
		print(url)
		
		https = await self.verifie_url(message)
		if https == True:
			print("Https == True")
			await self.play_url(message,url,True)

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
			
			spider = os.getcwd()

			if '/' in spider:
				spider = spider + '/yt_url_spider_v2.py'
			elif '\\' in spider:
				spider = spider + '\\yt_url_spider_v2.py'

			print(spider)
			url = text_to_url.url_find(spider,'https://www.youtube.com',str(msg_query_end)).get_complete_url()
			print(url)


			await self.play_url(message,url,True)
	
	async def queue(message):
		pass

	#antispam
	async def agreement(self,message):
		msg = await self.client.send_message(message.channel,"Veux tu jouer un meme audio aléatoire ? (clique sur ok)")
		await self.client.add_reaction(msg,emoji='✅')

		def check(reaction, user):
			return True
		
		time.sleep(2)
		res = await self.client.wait_for_reaction(emoji='✅',message=msg, check=check)

		while str(res.user).split('#')[0] != str(message.author.name):
			asyncio.sleep(1)
			res = await self.client.wait_for_reaction(emoji='✅',message=msg, check=check)

		return True

	def arg_meme_audio(message):
		pass#url,titre -url -title -list -u -t -l

	async def meme_audio(self,message):
		if message.content.endswith('-l'):
			msg_meme_audio = []

			for x in self.meme_audio_list:
				msg_meme_audio.append(await self.client.send_message(message.channel,x))

			await asyncio.sleep(10)

			for x in msg_meme_audio:
				await self.client.delete_message(x)
		else:
			await self.join(message,False)

			url = random.choice(self.meme_audio_list)
			await self.play_url(message,url,False,False)