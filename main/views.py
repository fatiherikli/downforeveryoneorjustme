# Create your views here.
import urllib
from django.http import HttpResponse
from django.shortcuts import render_to_response
from main.tasks import web_site_status

def home(request):
    return render_to_response('home.html')

def check(request):
    url = 'http://%s' % request.GET.get('url','google.com')
    job = web_site_status.delay(url)
    status_code = job.get() # wait for response.
    return HttpResponse(status_code)