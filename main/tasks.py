from celery.task import task
import requests

@task
def web_site_status(url):
    try:
        status_code = requests.get(url=url).status_code
    except Exception as e:
        status_code = 404
    print '%s   ---> %s' % (url, status_code)
    return status_code