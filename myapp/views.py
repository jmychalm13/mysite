from django.shortcuts import render
from django.http import HttpResponse
from pandas import pandas
from .models import Data
import json


# Create your views here.
def hello(request):
    if request.method == "POST":
        previous_data = Data.objects.all()
        previous_data.delete()
        file = request.FILES["file"]
        df = pandas.read_csv(file)
        json_records = df.reset_index().to_json(orient="records")
        data = []
        data = json.loads(json_records)
        for d in data:
            name = d["property_name"]
            price = d["property_price"]
            rent = d["property_rent"]
            emi = d["emi"]
            tax = d["tax"]
            exp = d["other_exp"]
            dt = Data(name=name, price=price, rent=rent, emi=emi, tax=tax, exp=exp)
            dt.save()
    else:
        print("This is a GET request")
    return render(request, "myapp/index.html")
