# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class SiteLanguage(models.Model):
	lang = models.NullBooleanField()
	
	def __unicode__(self):
		return u"%s" % (self.lang)

# user table
class UserExt(models.Model): 
	phone	= 	models.CharField(max_length=20, null=True, blank=True)
	city	= 	models.CharField(max_length=100, null=True, blank=True)
	defaultLanguage = models.CharField(max_length=2, null=True, blank=True)
	picture	=	models.FileField(upload_to='site_media/upload', null=True, blank=True) # picture of the user
	user 	= 	models.ForeignKey(User, unique=True)
	
	def __unicode__(self):
		return u"%s" % (self.user)
		
	User.profile = property(lambda u: UserExt.objects.get_or_create(user=u)[0])
		
# Social networks table
class SocialNetworks(models.Model):
	name 	=	models.CharField(max_length=50)
	
	def __unicode__(self):
		return u"%s" % (self.name)
	
# User-Networks link table
class UserSocialNetworks(models.Model):
	user			=	models.ForeignKey(User)	
	networkName		=	models.ForeignKey(SocialNetworks)	
	userLogin		=	models.CharField(max_length=50)
	
	def __unicode__(self):
		return u"%s - %s" % (self.user, self.networkName)

# documents table
class Document(models.Model):
	file		=	models.FileField(upload_to='upload') # sauve dans upload/ sous sitemedia
	type		=	models.CharField(max_length=100)
	description	=	models.TextField()
	date		=	models.DateTimeField('Uploaded')# Friday, September 04th 2011 at 10:30AM
	access		=	models.IntegerField()			# level access of the document
	user		=	models.ForeignKey(User) 		# who posted	
	
	def __unicode__(self):
		return u"%s - %s" % (self.type, self.file)

# events table
class Event(models.Model):
	date		=	models.DateTimeField('Time of event', null=True, blank=True)
	place		=	models.CharField(max_length=100)
	description	=	models.TextField()
	title		=	models.CharField(max_length=50)
	document	=	models.ForeignKey(Document, null=True, blank=True)	# pictures for example
	user		=	models.ForeignKey(User)			# who create it
	
	def __unicode__(self):
		return u"%s - %s" % (self.date, self.title)

# events-user link table
class EventUser(models.Model):
	user			=	models.ForeignKey(User)	
	event			=	models.ForeignKey(Event)
	
	def __unicode__(self):
		return u"%s - %s" % (self.event, self.user)
		
# newsletter table
class Newsletter(models.Model):
	recipient	=	models.CharField(max_length=100)	# everyone, promotion 2008 only, etc... 
	title		=	models.CharField(max_length=100)
	text		=	models.TextField()
	date		=	models.DateTimeField('Published')
	user		= 	models.ForeignKey(User)				# who create it
	
	def __unicode__(self):
		return u"%s - %s" % (self.date, self.title)
	
# cv table <=> personnal experiences
class CV(models.Model):
	user		=	models.ForeignKey(User)	# Tester si ca marche.. Clé étrangère en clé primaire
	beginDate	=	models.DateTimeField('Begin')		# 2008-2011	
	endDate		=	models.DateTimeField('End')
	place		=	models.CharField(max_length=100)	# IUT Paris Descartes, 143 Avenue de Versailles 75016 Paris
	jobDescr	=	models.TextField()					# DUT Informatique from 2008 to 2010 and then, etc... 
	type		=	models.CharField(max_length=100)	# Student/CDD/CDI/etc... 

	def __unicode__(self):
		return u"%s - %s" % (self.user, self.beginDate)
		
# year table
class Year(models.Model):
	year 		= 	models.CharField(max_length=15, primary_key=True) # 2008-2009
	description	= 	models.TextField(null=True, blank=True)
	
	def __unicode__(self):
		return u"%s" % (self.year)
	
# user-year link table
class UserYear(models.Model):
	user			=	models.ForeignKey(User)	
	year			=	models.ForeignKey(Year)	
	personnalExp	=	models.TextField(null=True, blank=True)
	
	def __unicode__(self):
		return u"%s - %s" % (self.user, self.year)
	
# jobs table
class Job(models.Model):
	type			=	models.CharField(max_length=100)	# searching/wanting
	title			=	models.CharField(max_length=100)
	description		=	models.TextField()
	agreementType	=	models.CharField(max_length=100, null=True, blank=True)	# stage/cdd/cdi...
	duration		=	models.CharField(max_length=50, null=True, blank=True)		# 6 month/2 years
	wages			=	models.FloatField(null=True, blank=True)					# 15€ per hour
	user			=	models.ForeignKey(User)
		
	def __unicode__(self):
		return u"%s - %s" % (self.type, self.title)
		
# pages table
# definition = edito (main column of home page), links, promo, textmining, webprogramming, etc.
# section : pour textmining = summary, wikipedia, pmi
# subsection : pour textmining/wikipedia = categories, biblio, etc.
class Page(models.Model):
	definition	=	models.CharField(max_length=100)
        subtopic        =       models.CharField(max_length=100, default='nil')
        subsubtopic     =       models.CharField(max_length=100, default='nil')
	titleFR		=	models.CharField(max_length=100)
	textFR		=	models.TextField()
	titleEN		=	models.CharField(max_length=100,  null=True, blank=True)
	textEN		=	models.TextField( null=True, blank=True)
	lastUpdate 	= 	models.DateTimeField('Updated')
	
	def __unicode__(self):
		return u"%s %s  %s" % (self.definition, self.subtopic, self.subsubtopic)
	
# comments table
class Comment(models.Model):
	date	=	models.DateTimeField('Published')
	title	=	models.CharField(max_length=100, null=True, blank=True)
	text	=	models.TextField()
	user	=	models.ForeignKey(User) 
	page	=	models.ForeignKey(Page) 
	
	def __unicode__(self):
		return u"%s - %s - page %s" % (self.date, self.title, self.page)
	
# documents-pages link table
class DocumentPage(models.Model):
	page	=	models.ForeignKey(Page) 
	doc		=	models.ForeignKey(Document) 
	
	def __unicode__(self):
		return u"Document %s in page %s" % (self.doc, self.page)
