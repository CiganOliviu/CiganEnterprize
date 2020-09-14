from django.contrib import admin
from .models import AvaibleJob, Studio, JobAppliance

class StudioAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'country')
    prepopulated_fields = {'studio_slug': ('city',)}

class AvaibleJobAdmin(admin.ModelAdmin):
    list_display = ('post', 'location')
    prepopulated_fields = {'job_slug': ('post',)}

class JobApplianceAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'carrer', 'date')


admin.site.register(Studio, StudioAdmin)
admin.site.register(AvaibleJob, AvaibleJobAdmin)
admin.site.register(JobAppliance, JobApplianceAdmin)
