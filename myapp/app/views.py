
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
def name(request):
    return HttpResponse("l'm Getu Haile")