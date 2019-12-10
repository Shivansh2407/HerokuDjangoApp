from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.conf import settings

def IndexView(request):
    return HttpResponse('Hello, World ! This is a Working HerokuApp By Shivansh Srivastava . Go to : www.github.com/Shivansh2407 for more interesting projects ')
