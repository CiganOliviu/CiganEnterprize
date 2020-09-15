from django.shortcuts import render
from django.shortcuts import reverse
from django.views import generic

from .models import Studio, JobsAppliance, AvaibleJob
from .forms import ApplianceForm

def index(request):

    template_name = 'views/index.html'

    return render(request, template_name)

def studio_lister(request):

    template_name = 'views/studios/studios_lister.html'

    studios_result = Studio.objects.all()

    context = {

        'studios_result' : studios_result,
    }

    return render(request, template_name, context)

class StudioDetail(generic.DetailView):

    model = Studio

    template_name = 'views/studios/studio_detail.html'

    slug_field = 'studio_slug'
    slug_url_kwarg = 'studio_slug'

def jobs_lister(request):

    template_name = 'views/jobs/jobs_lister.html'

    jobs_result = AvaibleJob.objects.all()

    context = {

        'jobs_result' : jobs_result,
    }

    return render(request, template_name, context)

class JobDetail(generic.DetailView):

    model = AvaibleJob

    template_name = 'views/jobs/job_detail.html'

    slug_field = 'job_slug'
    slug_url_kwarg = 'job_slug'

class JobAppliance(generic.TemplateView):

    template_name = 'views/carrers/job_appliance.html'
    final_template_name = 'views/carrers/job_appliance_send.html'

    def get(self, request):

        form = ApplianceForm()
        post = form.save(commit = False)

        args = { 'form' : form }

        return render(request, self.template_name, args)

    def _validate_save(self, database_name, database_object):

        if not JobsAppliance.objects.filter(first_name = post.first_name, last_name = post.last_name,
            email = post.email, years_of_experience = post.years_of_experience,
            description_of_skills = post.description_of_skills, carrer = post.carrer).exists():
            return True

        return False

    def post(self, request):

        form = ApplianceForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit = False)

            if self._validate_save():
                form.save()

        return render(request, self.final_template_name)
