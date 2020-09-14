from django.db import models

COUNTRY = (
    ("Romania", "Romania"),
)

class Studio(models.Model):

    city = models.CharField(max_length = 200, unique = True, default = "")
    address = models.CharField(max_length = 200, unique = True, default = "")
    country = models.CharField(max_length = 100, choices = COUNTRY, default = "Romania")
    description = models.TextField(default = "")
    studio_slug = models.SlugField(max_length = 200, unique = True, default = "")

    def __str__(self):

        return self.city

class AvaibleJob(models.Model):

    post = models.CharField(max_length = 150, unique = False, default = "")
    location = models.ForeignKey(Studio, on_delete = models.CASCADE, default = 1)
    description = models.TextField(default = "")
    requirements = models.TextField(default = "")
    one_day = models.TextField(default = "")
    released_day = models.DateTimeField(auto_now_add = True)
    job_slug = models.SlugField(max_length = 200, unique = True, default = "")

    def __str__(self):

        return str(self.post) + " " + str(self.location)

class JobAppliance(models.Model):

    first_name = models.CharField(max_length = 100, default = "")
    last_name = models.CharField(max_length = 100, default = "")
    email = models.EmailField(default = "")
    years_of_experience = models.PositiveIntegerField(default = 0)
    curriculum_vitae = models.FileField(upload_to = "curriculum_vitae/", default = 'default.pdf')
    description_of_skills = models.TextField(default = "")
    carrer = models.ForeignKey(AvaibleJob, on_delete = models.CASCADE, default = 1)

    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):

        return str(self.first_name) + " " + str(self.last_name)