from django.shortcuts import render
from django.http import HttpResponse #San Added
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password (request):
    
    characters = list('abcdefghijklmnopqrstuvwxys')

    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('Numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12)) #use default of 12 characters

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})