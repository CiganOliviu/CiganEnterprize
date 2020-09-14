from django.shortcuts import render

def newsletter(request):

    template_name = 'views/newsletter/newsletter.html'

    return render(request, template_name)

def formular_contact(request):

    template_name = 'views/formular/contact.html'

    return render(request, template_name)
