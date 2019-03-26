import asyncio
import discord
from constant_class import Juice_constants
Const = Juice_constants()

async def clear(client,message,amount=1):
	if await verifie_admin(client,message) == True:
		await asyncio.sleep(2)
		channel = message.channel
		
		for x in range(0,int(amount)+2):
			delete = client.logs_from(message.channel,limit=3)
			await client.delete_messages(delete)

		await client.say('Messages deleted.')

async def info(client,message):
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

async def verifie_admin(client,message):
		for x in Const.admin:
			if message.author.name == x:
				await client.send_message(message.channel,'You are {}, proceed ...'.format(message.author.name))
				return True

		await client.send_message(message.channel,'You are not an admin.')
		return False

async def close(client,message):
	if await verifie_admin(client,message) == True:
		await client.close()

class plug_in():
	def __init__(self,client):
		self.client = client