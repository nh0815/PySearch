__author__ = 'Nick Hirakawa'


from invdx import build_data_structures
from rank import *
from collections import OrderedDict
import operator
from db import cursor


class QueryProcessor:
	def __init__(self, idx, dlt, ft):
		#self.index, self.ft, self.dlt = build_data_structures(corpus)
		self.idx_file = idx
		self.dlt = dlt
		self.ft = ft

	def run_query_likelihood(self, query):
		mu = 2000
		print 'query:', query
		print "running query with mu=%d" % mu
		result = OrderedDict()  # collect document rankings for this value of mu
		curs = cursor()
		curs.execute('SELECT SUM(frequency) FROM Word')
		C, = curs.fetchone()
		curs.execute('SELECT COUNT(DISTINCT docid) FROM Document')
		D, = curs.fetchone()
		for term in query:
			print 'searching index'
			curs.execute('SELECT docid, freq FROM Entry WHERE word="%s"' % term)
			rows = curs.fetchall()
			print rows
			print 'found word in index:', term
			docs = set()
			print 'scoring documents'
			#score documents that contain term
			for docid, f in rows:
				docs.add(docid)
				curs.execute('SELECT frequency FROM Word WHERE word="%s"' % term)
				c, = curs.fetchone()
				score = score_query_likelihood(f=float(f), mu=mu, c=c, C=C, D=D)
				print term, docid, f, score
				print score
				if docid in result:
					result[docid] += score
				else:
					result[docid] = score

			print 'scoring other documents'
			#score documents that don't contain term
			tmp = [str(x) for x in range(D)]
			s = set(tmp).difference(docs)
			curs.execute('SELECT frequency FROM Word WHERE word="%s"' % term)
			c, = curs.fetchone()
			score = score_query_likelihood(f=0, mu=mu, c=c, C=C, D=D)
			print score
			for docid in s:
				if docid in result:
					result[docid] += score
				else:
					result[docid] = score
		return result

'''
	def run_BM25(self, query):
		query_result = dict()
		for term in query:
			if term in self.index:
				doc_dict = self.index[term] # retrieve index entry
				for docid, freq in doc_dict.iteritems(): #for each document and its word frequency
					score = score_BM25(n=len(doc_dict), f=freq, qf=1, r=0, N=len(self.dlt),
					                   dl=self.dlt.get_length(docid),
					                   avdl=self.dlt.get_average_length()) # calculate score
					if docid in query_result: #this document has already been scored once
						query_result[docid] += score
					else:
						query_result[docid] = score
		return query_result
'''

'''
	def run_QueryLikelihood(self, query):
		query_result = OrderedDict()
		for mu in mu_values:
			mu_result = dict()
			for term in query:
				if term in self.index:
					docs = set()
					#score documents containing term
					for docid, freq in self.index[term].iteritems():
						score = score_query_likelihood(f=freq, mu=mu, c=self.ft.get_frequency(term),
													   C=len(self.index), D=len(self.dlt))
						docs.add(docid)
						if docid in mu_result:
							mu_result[docid] += score
						else:
							mu_result[docid] = score
					a = [str(x) for x in range(len(self.dlt))]
					s = set(a).difference(docs)
					#score documents not containing term
					for docid in s:
						score = score_query_likelihood(f=0, mu=mu, c=self.ft.get_frequency(term), C=len(self.index), D=len(self.dlt))
						if docid in mu_result:
							mu_result[docid] += score
						else:
							mu_result[docid] = score
				else:
					score = score_query_likelihood(f=0, mu=mu, c=self.ft.get_frequency(term), C=len(self.index), D=len(self.dlt))
					for i in range(len(self.dlt)):
						if i in mu_result:
							mu_result[i] += score
						else:
							mu_result[i] = score
			query_result[mu] = mu_result
		return query_result
	'''

