from django.shortcuts import render

from .models import List

def home(request):
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items})

def about(request):
    my_name = "Carlos"
    context = {'name':my_name, 'last_name': 'Corrales'}
    return render(request, 'about.html', context)
