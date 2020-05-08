from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(reqeust):
    return HttpResponse("Login Success~~")