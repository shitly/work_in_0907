from django.shortcuts import render
from django.http import JsonResponse
from . import get_ip


# Create your views here.
def homepage(request):
    get = request.GET["ip"]
    return render(request, "ips/index.html", {"result": get_ip.main(get)})


def app(request):
    get = request.GET["ip"]
    return JsonResponse(get_ip.main(get))
