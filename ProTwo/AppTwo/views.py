from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1 style='text-align:center; color:red'> Welcome!!!</h1>"
                        "<h2 style='text-align:center; color:red'>Go to /users to \
                        see the list of user's information</h2>")
