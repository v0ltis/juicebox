import discord
import youtube_dl
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import scrapy

yt_url_spider= '''
url = ['https://www.youtube.com/results?search_query=overwatch+rap+battle']
#pywin32
#scrapy

import scrapy

class yt_url_spider(scrapy.Spider):
    global url
    name = 'yt_url'
    start_urls = url
    def parse(self, response):
        for url in response.css("div div div div div div div div div h3 a"):
yield {'url_text': url.xpath('@href').extract_first()}
'''

my_directory= '''
import os

my_folder = ''
Pr = 1

class dir_location():

    def __init__(self):
        self.me = my_folder
        self.pr = Pr

    def search(self):
        a = str(os.getcwd())
        a = a.split('\\')
        #print(a)
        b = len(a)
        c = str(a[0]) + str('\\')
        for x in range(1,b):
            c = c + str(a[x]) + str('\\')
        self.me = c
        if self.pr == 1:
            print(self.me)
            
    def go_to_folder(self,Where):
        a = self.me + str(Where) + str('\\')
        self.me = a
        if self.pr == 1:
            print(self.me)
            
    def go_to_file(self,Where):
        a = self.me + str(Where)
        self.me = a
        if self.pr == 1:
            print(self.me)
            
    def back(self,Nb=1):
        a = self.me.split('\\')
        #print(a)
        b = len(a)
        #print(b)
        b -= Nb
        #print(b)
        #print(Nb)
        c = str(a[0]) + str('\\')
        for x in range(1,(b-1)):
            c = c + str(a[x]) + str('\\')
        self.me = c
        if self.pr == 1:
            print(self.me)
            
    def log(self,W=0):
        self.pr = W
'''

text_to_url = '''
import os
import json

class url_find():

  def __init__(self,file_py,file_json,main_url,query,att_url='',complete_url='',query_url=''):
    self.file_py = file_py
    self.file_json = file_json
    self.main_url = main_url
    self.query = query
    self.att_url = att_url
    self.me = my_directory.dir_location()
    self.query_url = query_url

    ytb_query = "https://www.youtube.com/results?search_query="
    query_splited = query.split(' ')

    query_builted = ''
    x = 0

    for x in range(0,len(query_splited)-1):
      query_builted = query_builted + query_splited[x] + '+'
    query_builted = query_builted + query_splited[x+1]
    ytb_query = ytb_query + query_builted
    self.query_url = ytb_query


  def read_values_from_json(self,file,key):
    values = []
    with open(file) as f:
      data = json.load(f)
      for entry in data:
        values.append(entry[key])
    return values

  def search(self):
    results = self.read_values_from_json("quotes.json","url_text")
    return results

  def reset_file(self,file):
    self.me.search()
    self.me.go_to_file(file)
    file = open(self.me.me ,'w')
    file.write("")
    file.close()
  
  def query_edit(self):
    self.me.search()
    self.me.go_to_file(self.file_py)
    file = open(self.me.me , 'r')
    query_edit_read = file.read()
    file.close()

    #split the first line in query_edit_read_spilted_lines
    query_edit_read_splited_lines = query_edit_read.splitlines()[0].split("'")
    query_edit_read_splited_lines[1] = self.query_url

    query_edit_write = []
    query_edit_write_splited_lines = ''

    #build the new first line
    for x in range(0,2):
      query_edit_write_splited_lines = query_edit_write_splited_lines + query_edit_read_splited_lines[x] + "'"
    query_edit_write_splited_lines = query_edit_write_splited_lines + query_edit_read_splited_lines[x+1]

    query_edit_write.append(query_edit_write_splited_lines)
    for x in query_edit_read.splitlines():
      if x != query_edit_read.splitlines()[0]:
        query_edit_write.append(x)
    
    query_edit_write_end = ''
    for x in query_edit_write:
      query_edit_write_end = query_edit_write_end + x + '\n'

    file = open(self.me.me, 'w')
    file.write(query_edit_write_end)
    file.close()

  def get_complete_url(self):
    debug = 0
    for x in self.query.split('.'):
      if x == 'youtube':
        debug += 1
      if x == 'com':
        debug += 1
      if x == 'watch':
        debug += 1

    if debug >= 3:
      return self.query

    self.reset_file(self.file_json)
    self.query_edit()
    os_command = "scrapy runspider " + str(self.file_py) + " -o " + str(self.file_json)
    os.system(os_command)

    _url = self.search()
    complete_url = self.main_url + _url[0]
    
    self.att_url = _url[0]
    self.complete_url = complete_url

    return complete_url

'''

exec(my_directory)
exec(text_to_url)



client = commands.Bot(command_prefix = '/')

merde = ["MERDE"]
chat_filter = ["PUTE","SALOPE","CONNARD","CUL","ABRUTIT","NIQUE","ENCULE","CHATTE","BITE","CON","BITCH","PUTIN","FOUTRE","ASS","TRISO","GOGOL","COQUIN","BATARDE","FELATION","SEX","VTFF","NTM"]
bypass_list = ["362615539773997056","437289213616979968"]

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="/help"))
    print("Logged in as:", client.user.name)
    print("ID:", client.user.id)
    
    
players = {}

@client.event
async def on_message(message):    
    if message.content.upper().startswith("/PING"):
      timePing = time.monotonic()
      pinger = await client.send_message(message.channel, ":ping_pong: **Pong !**")
      ping = "%.2f"%(1000* (time.monotonic() - timePing))
      await client.edit_message(pinger, ":ping_pong: **Pong !**\n\
`Ping:" + ping + "`")
        
    if message.content.upper().startswith("/SAY"):
          args = message.content.split(" ")
          await client.send_message(message.channel, (" ".join(args[1:])))
    contents = message.content.split(" ")
    for word in contents:
           if word.upper() in chat_filter:
             if not message.author.id in bypass_list:
                await client.delete_message(message)
                await client.send_message(message.channel, "**Hey!** un peut de respect!!!")
              
    if message.content.upper().startswith("/HELP"):
        help = discord.Embed(title='Commandes:', description='Voici la liste des commandes', colour=0x7a2581)
        help.set_author(name='Juicebox', icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
        help.add_field(name="Prefix:", value="/", inline=False)
        help.add_field(name="/help", value="Affiche les commandes", inline=True)
        help.add_field(name="/say (+texte)", value="Fait dire au bot le texte", inline=True)
        help.add_field(name="/ping", value="Affiche le ping", inline=True)
        help.add_field(name="/musique", value="donne les commandes musicales du bot", inline=False)
        await client.send_message(message.channel, embed=help)
                   
    if message.content.upper().startswith("/MUSIQUE"):
        musique = discord.Embed(title='Commandes musicales:', description='Voici la liste des commandes de la musique', colour=0x7a2581)
        musique.set_author(name='Juicebox', icon_url="https://discordemoji.com/assets/emoji/JuiceBox.png")
        musique.add_field(name=" /join :", value="Fait rejoindre juicebox dans votre salon vocal ", inline=True)
        musique.add_field(name="/play (+URL) :", value=" lis la video/musique (l'URL doit être un URL YouTube) ", inline=True)
        musique.add_field(name=" /stop", value="Arette la video", inline=True)
        musique.add_field(name="/pause", value="Met en pause la video", inline=True)
        musique.add_field(name="/resume", value="Reprend la video", inline=True)
        musique.add_field(name="/leave", value="Fait quitter juiceBox de votre salon vocal", inline=True)
        await client.send_message(message.channel, embed=musique)
        
       
    if message.content.upper().startswith("XD"):
       await client.send_message(message.channel,"lol")

    if message.content.startswith("🖕"):
       await client.send_message(message.channel,":rage:")

    for word in contents:
           if word.upper() in merde:
                await client.delete_message(message)
                await client.send_message(message.channel, ":shit:")
                
    if message.content.upper().startswith("YO"):
       await client.send_message(message.channel,"plait")

    if message.content.upper().startswith("BONJOUR"):
       await client.send_message(message.channel,"Hey!")

    if message.content.upper().startswith("GG"):
       await client.send_message(message.channel,":clap: :clap: :clap:") 

    if message.content.upper().startswith("/BOTADMIN"):
        await client.delete_message(message)
        await client.send_message(message.channel,"Hey Boss , code here: https://github.com/v0ltis/juicebox/edit/master/index.py")
    
    

    #join
    if message.content.upper().startswith("/JOIN"):
        channel = message.author.voice.voice_channel
        print("I'm connected to : " + str(channel))
        await client.join_voice_channel(channel)

    #play + query
    if message.content.upper().startswith("/PLAY"):
      print(message.content)
      message_url = message.content
      url = message_url.split(" ")[1]
      if len(message_url.split(" ")) == 1:
        message_channel = message.channel
        message_content = "Je vais avoir besoin d'un url"
        await client.send_message(message_channel,message_content)
      if len(message_url.split(" ")) >= 2:
        debug = 0
        for x in message_url.split("://"):
          if x == 'https':
            debug += 1
        if debug >= 1:
          print(url)
          print("I'm taking the first way !")
          server = message.server
          voice_client = client.voice_client_in(server)
          player = await voice_client.create_ytdl_player(url)
          players[server.id] = player

          try:
            player.start()
            message_channel = message.channel
            print("Let's play : " + str(url))
            message_content = "C'est parti pour : " + str(url)
            await client.send_message(message_channel,message_content)

          except:
            message_channel = message.channel
            message_content = "Buuuuuuuuuuug ... ça ne viens pas forcement de moi , essayez avec un autre URL YouTube. \n Url: " + str(url)
            await client.send_message(message_channel,message_content)

        else:
          print("I'm taking the second way !")
          msg_query = message.content.split(' ')
          msg_query.pop(0)

          msg_query_end = ''
          x=0

          for x in range(len(msg_query)-1):
            msg_query_end = msg_query_end + msg_query[x] + ' '
            
          msg_query_end = msg_query_end + msg_query[x+1]
          print(msg_query_end)
          url =text_to_url.url_find('yt_url_spider.py','quotes.json','https://www.youtube.com',str(msg_query_end)).get_complete_url()
          print(url)
          server = message.server
          voice_client = client.voice_client_in(server)
          player = await voice_client.create_ytdl_player(url)
          players[server.id] = player

          try:
            player.start()
            message_channel = message.channel
            print("Let's play : " + str(url))
            message_content = "C'est parti pour : " + str(url)
            await client.send_message(message_channel,message_content)

          except:
            message_channel = message.channel
            message_content = "Buuuuuuuuuuug ... ça ne viens pas forcement de moi , essayez avec un autre URL YouTube. \n Url: " + str(url)
            await client.send_message(message_channel,message_content)

    #pause
    if message.content.upper().startswith("/PAUSE"):
      id = message.server.id
      players[id].pause()
      message_channel = message.channel
      message_content = "Pause :+1:"
      await client.send_message(message_channel,message_content)

    
    #resume
    if message.content.upper().startswith("/RESUME"):
      id = message.server.id
      players[id].resume()
      message_channel = message.channel
      message_content = "Je recomence"
      await client.send_message(message_channel,message_content)


    #STOP
    if message.content.upper().startswith("/STOP"):
      id = message.server.id
      players[id].stop()
      message_channel = message.channel
      message_content = "Ok , ok , j'arrete"
      await client.send_message(message_channel,message_content)


    #leave
    if message.content.upper().startswith("/LEAVE"):
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

client.run(os.environ['TOKEN_BOT'])
