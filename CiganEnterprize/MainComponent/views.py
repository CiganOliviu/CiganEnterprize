from django.shortcuts import render
from django.shortcuts import reverse
from django.views import generic
from django.views.generic import edit
from .models import Studio, AvaibleJob
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
