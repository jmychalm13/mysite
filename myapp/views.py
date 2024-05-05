from django.shortcuts import render
from django.http import HttpResponse
from pandas import pandas


# Create your views here.
def hello(request):
    if request.method == "POST":
        file = request.FILES["file"]
        df = pandas.read_csv(file)
    else:
        print("This is a GET request")
    return render(request, "myapp/index.html")
