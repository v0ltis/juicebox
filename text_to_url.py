import my_directory
import subprocess
import os

class url_find():

	def __init__(self,file_py,main_url,query,att_url='',complete_url='',query_url=''):
		self.file_py = file_py
		self.main_url = main_url
		self.query = query
		self.att_url = att_url
		self.me = my_directory.dir_location()
		self.query_url = query_url
		ytb_query = '''https://www.youtube.com/results?search_query='''
		query_splited = query.split(' ')

		query_builted = ''
		x = 0

		for x in range(0,len(query_splited)-1):
			print(len(query_splited))
			query_builted = query_builted + query_splited[x] + '+'
		try:
			query_builted = query_builted + query_splited[x+1]
		except:
			pass
		
		ytb_query = ytb_query + query_builted
		print(ytb_query)
		self.query_url = ytb_query
	def me(arg):
		a = str(os.getcwd())
		if a.startswith('/'):
			args_ext = []
			a = a +'/'+arg
			return a

		else:
			a = a.split('\\')
			print(a)
			#print(a)
			b = len(a)
			c = str(a[0]) + str('\\')
			for x in range(1,b):
				c = c + str(a[x]) + str('\\')
			d = arg
			c = c + d
			return c

	def get_complete_url(self):
		a = subprocess.check_output("ls").decode()
		print(a)
		os_command = "scrapy runspider " + url_find.me(str(self.file_py)) +''' -a url="%s"''' % self.query_url
		print(os_command)
		a = subprocess.check_output(os_command).decode()
		print(a)
		for x in range(0,10):
			print(a)
		complete_url = self.main_url + a
		return complete_url
'''
#Test
get_url = url_find('yt_url_spider_v2.py','youtube.com','windows error song').get_complete_url()
print(get_url)
'''