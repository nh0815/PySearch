
from django.shortcuts import render, redirect
from django.http import HttpResponse

__author__ = 'Nick'


def index(request):
	return redirect('/search')