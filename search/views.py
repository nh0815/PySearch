from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
from engine.query import QueryProcessor
from engine.invdx import InvertedIndex, DocumentLengthTable, WordFrequencyTable
from engine.parse import CorpusParser
from engine.db import cursor
import os

# Create your views here.

# set up data structures
dlt = DocumentLengthTable()
dlt.read('index/length.txt')
wft = WordFrequencyTable()
wft.read('index/freq.txt')
proc = QueryProcessor('index/index.txt', dlt, wft)

# read documents for retrieval
cp = CorpusParser('index/corpus.txt')
cp.parse()
docs = cp.get_corpus()


def index(request):
	return render(request, 'search/index.html', {})


def query(request):
	query = request.GET.get('query').split(' ')
	results = proc.run_query_likelihood(query)
	return HttpResponse(dumps(results))


def doc(request):
	docid = int(request.GET.get('doc'))
	curs = cursor()
	curs.execute('SELECT text FROM Document WHERE docid="%d"' % docid)
	doc_text, = curs.fetchone()
	text = {'text': doc_text}
	return HttpResponse(dumps(text))


if __name__ == '__main__':
	cp = CorpusParser('index/corpus.txt')
	cp.parse()
	docs = cp.get_corpus()