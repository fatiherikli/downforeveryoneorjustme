# Create your views here.
import urllib
from django.http import HttpResponse
from django.shortcuts import render_to_response
from main.tasks import web_site_status

def home(request):
    return render_to_response('home.html')

def check_direct(request):
    url = request.GET.get('url','http://google.com')
    status = web_site_status(url)
    return HttpResponse(status)