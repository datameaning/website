from website.myapp.models import SiteLanguage, UserExt, SocialNetworks, UserSocialNetworks, Document, Event, EventUser, Newsletter, CV, Year, UserYear, Job, Page, Comment, DocumentPage
from django.contrib import admin

# Editer pour ajouter les photos liees a une page
class PageAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 			{'fields': ['definition', 'subtopic', 'subsubtopic' ,'lastUpdate']}),
		('Francais', 	{'fields': ['titleFR', 'textFR']}),
		('English', 	{'fields': ['titleEN', 'textEN']}),
	]

admin.site.register(SiteLanguage)
admin.site.register(UserExt)
admin.site.register(SocialNetworks)
admin.site.register(UserSocialNetworks)
admin.site.register(Document)
admin.site.register(Event)
admin.site.register(EventUser)
admin.site.register(Newsletter)
admin.site.register(CV)
admin.site.register(Year)
admin.site.register(UserYear)
admin.site.register(Job)
admin.site.register(Page, PageAdmin)
admin.site.register(Comment)
admin.site.register(DocumentPage)

