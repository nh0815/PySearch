__author__ = 'Nick'


from urllib2 import *
from json import *

def build_db(route):
	url = 'http://localhost:5984/%s' % route
	print url
	try:
		urlopen(url)
	except HTTPError:
		opener = build_opener(HTTPHandler)
		request = Request(url)
		request.get_method = lambda: 'PUT'
		url = opener.open(request)

def bulk_load(route, docs):
	build_db(route)
	data = dumps(docs)
	opener = build_opener(HTTPHandler)
	url = 'http://localhost:5984/%s/_bulk_docs' % route
	request = Request(url, data=data)
	request.add_header('Content-Type', 'application/json')
	request.get_method = lambda: 'POST'
	opener.open(request)


class CouchDBHandler(HTTPHandler):

	def __init__(self):
		self.path = 'http://localhost:5984/'

	def get(self, route):
		url = self.path + route
		try:
			data =urlopen(url)
			return loads(''.join(data.readlines()))
		except HTTPError:
			return {}

	def get_term_frequency(self, word):
		url = self.path + 'index/' + word
		try:
			data = urlopen(url)
			return loads(data.readlines()[0])
		except HTTPError:
			return {}

	def get_word_frequency(self, word):
		url = self.path + 'word_freq/' + word
		try:
			data = urlopen(url)
			return loads(data.readlines()[0])
		except HTTPError:
			return 0

	def get_doc_freq(self, docid):
		url = self.path + 'doc_freq/' + docid
		try:
			data = urlopen(url)
			return loads(data.readlines()[0])
		except HTTPError:
			return 0

	def get_doc_count(self, route):
		url = self.path + route + '/_all_docs'
		try:
			data = urlopen(url)
			return loads(''.join(data.readlines()))['total_rows']
		except HTTPError:
			return 0

class PostRequest(Request):

	def __init__(self):
		self.get_method = lambda: 'POST'
		self.add_header('Content-Type', 'application/json')


if __name__ == '__main__':
	db = CouchDBHandler()
	print db.get_doc_count('doc_freq')