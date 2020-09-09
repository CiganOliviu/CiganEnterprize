from django.shortcuts import render, redirect
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Job, Sedium, Event

def index(request):

    template_name = 'views/index.html'

    return render(request, template_name)

def jobs_search_view (request):

    template_name = 'views/jobs/search.html'

    query = request.GET.get('q')

    if query:
        results = Job.objects.filter(Q(post__icontains = query))
    else:
        return redirect('/jobs')

    context = {
        'results' : results
    }

    return render(request, template_name, context)

class JobsList(generic.ListView):

    queryset = Job.objects.all()

    template_name = 'views/jobs/jobs.html'

class JobDetail(generic.DetailView):

    model = Job

    template_name = 'views/jobs/jobs_detail.html'

class SediumsList(generic.ListView):

    queryset = Sedium.objects.all()

    template_name = 'views/sediums/sediums.html'

class SediumDetail(generic.DetailView):

    model = Sedium

    template_name = 'views/sediums/sedium_detail.html'

class EventsList(generic.ListView):

    queryset = Event.objects.all()

    template_name = 'views/events/events.html'

class EventDetail(generic.DetailView):

    model = Event

    template_name = 'views/events/event_detail.html'
