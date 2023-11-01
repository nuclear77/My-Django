from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Главная</h1>')


def about(request):
    return HttpResponse('<h1>2 страница</h1>')


def logo(request):
    return HttpResponse('<h1>3 страница</h1>')


