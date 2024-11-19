from django.http import HttpResponse, JsonResponse
from .tasks import send_email_task
from django.core.cache import cache
import requests

from django.views.decorators.cache import cache_page


def send_email(request):
    send_email_task.delay()
    return HttpResponse("<h1>Done Sending</h1>")

@cache_page(60)
def test(request):
    response = requests.get("url")
    return JsonResponse(response.json())
