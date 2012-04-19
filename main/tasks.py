# coding: latin1
import urllib
from celery.task import task

@task
def web_site_status(url):
    return urllib.urlopen(url).getcode()