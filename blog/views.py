from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. by myself


def index(request):
    return render(request, "blog/index.html")
