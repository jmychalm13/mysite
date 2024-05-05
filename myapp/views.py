from django.shortcuts import render
from django.http import HttpResponse
from pandas import pandas
import json


# Create your views here.
def hello(request):
    if request.method == "POST":
        file = request.FILES["file"]
        df = pandas.read_csv(file)
        json_records = df.reset_index().to_json(orient="records")
        data = []
        data = json.loads(json_records)
        print(data)
    else:
        print("This is a GET request")
    return render(request, "myapp/index.html")
