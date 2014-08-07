__author__ = 'Nick Hirakawa'

import re
from collections import OrderedDict


class CorpusParser:

	def __init__(self, filename):
		self.filename = filename
		self.regex = re.compile('^#\s*\d+')
		self.corpus = OrderedDict()

	def parse(self):
		with open(self.filename) as f:
			s = ''.join(f.readlines())
		blobs = s.split('#')[1:]
		for x in blobs:
			text = x.split()
			docid = text.pop(0)
			self.corpus[docid] = ' '.join(text)

	def get_corpus(self):
		return self.corpus


class QueryParser:

	def __init__(self, filename):
		self.filename = filename
		self.queries = []

	def parse(self):
		with open(self.filename) as f:
			lines = ''.join(f.readlines())
		self.queries = [x.rstrip().split() for x in lines.split('\n')[:-1]]

	def get_queries(self):
		return self.queries


if __name__ == '__main__':
	cp = CorpusParser('../index/corpus.txt')
	cp.parse()
	docs = cp.get_corpus()
	with open('docs.txt', 'w') as d:
		for doc in docs:
			d.write(doc)
			d.write('\t')
			d.write(str(len(docs[doc])))
			d.write('\t')
			d.write(docs[doc])
			d.write('\n')