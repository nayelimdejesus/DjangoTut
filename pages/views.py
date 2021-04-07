from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1> Hello World </h1>") #string of HTML Code

# def contact_view(*args, **kwargs):
#     return HttpResponse("<h1> This is the contact page!</h1>")