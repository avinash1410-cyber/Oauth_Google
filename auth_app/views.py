
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    user=request.user
    return HttpResponse(f"This works Mr {user}")
