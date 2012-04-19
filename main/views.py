# Create your views here.
import urllib
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html')

def check(request):
    url = 'http://%s' % request.GET.get('url','google.com')
    status_code = urllib.urlopen(url).getcode()
    return HttpResponse(status_code)