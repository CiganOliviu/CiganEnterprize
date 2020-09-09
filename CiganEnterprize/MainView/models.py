from django.db import models
from django.urls import reverse

class Sedium(models.Model):

    city = models.CharField(max_length = 200, blank = False)
    address = models.CharField(max_length = 200, blank = False)
    description = models.TextField(blank = False)
    jobs = models.ManyToManyField('Job')
    sedium_slug = models.SlugField(max_length = 200, unique = True, default = '')


    def __str__(self):

        return self.city

    def get_absolute_url(self):

        return reverse('sedium_detail', args=[str(self.id)])

class Job(models.Model):

    post = models.CharField(max_length = 200, blank = False)
    location = models.ForeignKey(Sedium, on_delete = models.CASCADE, related_name = 'sedium_posts', default = 1)
    description = models.TextField(blank = False)
    requirements = models.TextField(blank = False)
    a_day_at_job = models.TextField(blank = False)
    released = models.DateTimeField(auto_now_add = True)

    slug = models.SlugField(max_length = 200, unique = True, default = '')

    def __str__(self):

        return self.post

class Event(models.Model):

    theme_title = models.CharField(max_length = 200, blank = False)
    about_theme = models.TextField(max_length = 200, blank = False)
    country = models.CharField(max_length = 200, blank = False)
    city = models.CharField(max_length = 200, blank = False)
    place = models.CharField(max_length = 200, blank = False)
    date = models.DateTimeField()
    tickets = models.URLField(max_length = 200)

    def __str__(self):

        return self.theme_title

    def get_absolute_url(self):

        return reverse('event_detail', args=[str(self.id)])
