from django.db import models

# Create your models here.


class Word(models.Model):
	word = models.CharField(max_length=30)


class Document(models.Model):
	docid = models.IntegerField(default=-1)


class Entry(models.Model):
	word = models.ForeignKey('Word', primary_key=True)
	docid = models.ForeignKey('Document', primary_key=True)
	freq = models.IntegerField(default=0)