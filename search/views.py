from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'search/index.html', {})

def query(request):
	query = request.GET.get('asdf')
	return HttpResponse(query)