from django.contrib import admin
from .models import Job, Sedium, Event

class JobAdmin(admin.ModelAdmin):
    list_display = ('post', 'released')
    prepopulated_fields = {'slug': ('post', )}

class SediumAdmin(admin.ModelAdmin):
    list_display = ('city', 'address')
    prepopulated_fields = {'sedium_slug': ('city', )}

class EventAdmin(admin.ModelAdmin):
    list_display = ('theme_title', 'country', 'city', 'date')

admin.site.register(Job, JobAdmin)
admin.site.register(Sedium, SediumAdmin)
admin.site.register(Event, EventAdmin)
