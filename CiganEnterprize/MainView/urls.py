from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('jobs/results/', views.jobs_search_view, name='search_view'),
    path('jobs/', views.JobsList.as_view(), name='jobs_list'),
    path('sediums/', views.SediumsList.as_view(), name='sediums_list'),
    path('events/', views.EventsList.as_view(), name='events_list'),

    path('sediums/<int:pk>/', views.SediumDetail.as_view(), name='sedium_detail'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event_detail'),
    path('jobs/<slug:slug>/', views.JobDetail.as_view(), name='job_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
