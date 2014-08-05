from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
from engine.query import QueryProcessor
from engine.invdx import InvertedIndex, DocumentLengthTable, WordFrequencyTable
import os

# Create your views here.

dlt = DocumentLengthTable()
dlt.read('index/length.txt')
wft = WordFrequencyTable()
wft.read('index/freq.txt')
proc = QueryProcessor('index/index.txt', dlt, wft)

def index(request):
	return render(request, 'search/index.html', {})

def query(request):
	query = request.GET.get('query').split(' ')
	results = proc.run_query_likelihood(query)
	return HttpResponse(dumps(results))