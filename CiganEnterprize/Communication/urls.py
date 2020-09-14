from django.urls import path

from . import views

urlpatterns = [
    path('newsletter/', views.newsletter, name = 'newsletter'),
    path('contact/', views.formular_contact, name = 'formular_contact'),
]
