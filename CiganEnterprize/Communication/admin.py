from django.contrib import admin
from .models import NewsLetter, Contact

class NewsletterAdmin(admin.ModelAdmin):
    display_list = ('email', 'date')

class ContactAdmin(admin.ModelAdmin):
    display_list = ('last_name', 'title')

admin.site.register(NewsLetter, NewsletterAdmin)
admin.site.register(Contact, ContactAdmin)
