from django.shortcuts import render
from django.http import HttpResponse
from chefs.models import Chef
from .models import Gallery, Events, Contacts


# Create your views here.
def home_view(request):
    # return HttpResponse('<h1>This is future home page</h1>')
    # chefs = Chef.objects.all()
    chefs = Chef.objects.filter(is_visible=True).order_by('position')
    gallery = Gallery.objects.filter(is_visible=True).order_by('position')
    events = Events.objects.filter(is_visible=True).order_by('position')
    contacts = Contacts.objects.first()
    # return render(request, 'layouts/home.html')
    return render(request, 'index2.html', {
        'chefs': chefs,
        'gallery': gallery,
        'events': events,
        'contacts': contacts,
    })
