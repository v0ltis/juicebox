import os
import my_directory
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

		ytb_query = '''https://www.youtube.com/results?search_query='''
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
#Test
get_url = url_find('yt_url_spider.py','quotes.json','youtube.com','windows error song').get_complete_url()
print(get_url)
'''
