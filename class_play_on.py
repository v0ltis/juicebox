import asyncio
import discord

class ready():
	def __init__(self,client):
		self.client = client
	
	async def boucle(self):
		while True:
			nb_of_serv_where_i_am_connected = 0
			for x in self.client.servers:
				nb_of_serv_where_i_am_connected += 1
				serv_co = str(nb_of_serv_where_i_am_connected) + ' serveurs'

			await self.client.change_presence(status=discord.Status.dnd,game=discord.Game(name=serv_co,type=0))
			await asyncio.sleep(15)
			await self.client.change_presence(status=discord.Status.dnd,game=discord.Game(name="/help",type=0))
			await asyncio.sleep(15)
			await self.client.change_presence(status=discord.Status.dnd,game=discord.Game(name="juicebot.github.io",type=0))
			await asyncio.sleep(15)
			await self.client.change_pressence(status=discord.Status.dnd,game=discord.Game(name="Version:1.9",type=0))
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
		for x in self.client.servers:
			await client.send_message(discord.Object(id="547731369988587530", server.owner.id)
