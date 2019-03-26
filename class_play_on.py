import asyncio
import discord

from constant_class import Juice_constants
Const = Juice_constants()

class Ready():
	def __init__(self):
		self.client =  Const.client
	
	async def boucle(self):
		while True:
			nb_of_serv_where_i_am_connected = 0
			for x in self.client.servers:
				nb_of_serv_where_i_am_connected += 1
				serv_co = str(nb_of_serv_where_i_am_connected) + ' serveurs'

			await self.client.change_presence(game=discord.Game(name=serv_co))
			await asyncio.sleep(15)
			await self.client.change_presence(game=discord.Game(name="/help"))
			await asyncio.sleep(15)
			await self.client.change_presence(game=discord.Game(name="juicebot.github.io"))
			await asyncio.sleep(15)
	
	async def upload_juice_emoji(self):
			juiceboxemoji = False
			for x in self.client.servers:
				for y in x.emojis:
					if y.name == "JuiceBox":
						#already this emoji
						juiceboxemoji = True
				if juiceboxemoji == False:
					await self.client.create_custom_emoji(x,name='JuiceBox',image=open('JuiceBot.png','rb').read())
				else:
					juiceboxemoji = False
	
	async def ready(self):
		print("Logged in as:", self.client.user.name)
		print("ID:", self.client.user.id)
		try:
			await self.client.send_message(discord.Object(id='543490625773895681'), 'Redemarage effectué !')
		except:
			print("Not allowed.(ready fonction,redemarage effectué!)")
		#switch entre serv_co /help et juice...
		await self.boucle()
		
		#upload l'emoji juicebot sur tout les serveurs
		await self.upload_juice_emoji()