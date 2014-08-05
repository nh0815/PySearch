__author__ = 'Nick'

from django.conf.urls import url
from search import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^query/$', views.query, name='query'),
	url(r'^document/$', views.doc, name='document')
]