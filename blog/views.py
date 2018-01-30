from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. by other developer


def index(request):
    return render(request, "blog/index.html")
