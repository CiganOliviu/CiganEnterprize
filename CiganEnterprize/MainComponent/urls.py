from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('studios/', views.studio_lister, name = 'studio_lister'),
    path('jobs/', views.jobs_lister, name = 'jobs_lister'),

    path('studios/<slug:studio_slug>/', views.StudioDetail.as_view(), name='studio_detail'),
    path('jobs/<slug:job_slug>/', views.JobDetail.as_view(), name='job_detail'),
]
