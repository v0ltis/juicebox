import discord
import asyncio
import os
from constant_class import Juice_constants
import json
import aiohttp

client.

GIPHY_KEY = os.environ["TOKEN_GIPHY"]

async def gifsearch(client,message):
	linkstart = "http://api.giphy.com/v1/gifs/search?q="
	linkmiddle = "&api_key="
	linkend = "&limit=1"
	arg = "message.content"
	mess = "".join(arg[5:])
	lien = str(linkstart) + str(mess) + str(linkmiddle) + str(GIPHY_KEY) + str(linkend)
	async with aiohttp.ClientSession() as data:
		gif = json.dumps(lien, sort_keys=True, indent=4)
	await client.send_message(message.channel, gif)
	
