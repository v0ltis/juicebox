import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from class_add_on import clear

class ready():
	def __init__(self,client):
		self.client = client
	async def owner(self):
		for x in self.client.servers:
			owner = x.owner
			await self.client.send_message(discord.Object(id="547731369988587530"), owner)
			await self.client.send_message(x.owner, "Bonjour , nous voulions vous remercier d'utiliser JuiceBox et de votre patience envers ses 10h de down !\n\
Je vous invite également a rejoindre notre serveur discord : discord.gg/Abfvn9y\n\
Merci , Voltis#1234 de l'équipe de JuiceBox")

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
			await self.client.change_presence(status=discord.Status.dnd,game=discord.Game(name="Version:1.9",type=0))
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
		try:
			await self.owner()
		except:
			pass
		await self.boucle()
		#upload l'emoji juicebot sur tout les serveurs
		await self.upload_juice_emoji()
		#switch entre serv_co /help et juice...
		
