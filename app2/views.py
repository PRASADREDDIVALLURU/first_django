from django.shortcuts import render
from django.http import HttpResponse
def fun(request):
    return HttpResponse("<marquee><h1>i am prasad </h1></marquee>")
