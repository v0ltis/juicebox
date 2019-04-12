import discord
import asyncio
import os
from constant_class import Juice_constants
import urllib,json

GIPHY_KEY = os.environ["TOKEN_GIPHY"]

def gifsearch(message):
	linkstart = "http://api.giphy.com/v1/gifs/search?q="
	linkmiddle = "&api_key="
	linkend = "&limit=1"
	arg = "message.content"
	mess = "".join(arg[5:])
	lien = str(linkstart) + str(mess) + str(linkmiddle) + str(GIPHY_KEY) + str(linkend)
	
	data = json.loads(urllib.urlopen(lien).read())
	
	gif = json.dumps(data, sort_keys=True, indent=4)

	await client.send_message(message.channel, gif)
	
