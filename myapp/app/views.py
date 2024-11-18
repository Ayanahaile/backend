
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
def name(request):
    return HttpResponse("l'm Getu Haile")
def hobby(request):
    response_text = 'name: Getu Haile, football: playing and watching football, read: reading books'
    return HttpResponse(response_text)