from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    my_name = "Carlos"
    context = {'name':my_name, 'last_name': 'Corrales'}
    return render(request, 'about.html', context)
