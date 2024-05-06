from django.shortcuts import render
from django.http import HttpResponse
from pandas import pandas
from .models import Data
import json


# Create your views here.
def hello(request):
    if request.method == "POST":
        # getting any old data and deleting
        previous_data = Data.objects.all()
        previous_data.delete()
        # getting files from html
        file = request.FILES["file"]
        df = pandas.read_csv(file)
        # reorienting index
        json_records = df.reset_index().to_json(orient="records")
        data = []
        # putting json data into a list to work with
        data = json.loads(json_records)
        # looping through data
        for d in data:
            name = d["property_name"]
            price = d["property_price"]
            rent = d["property_rent"]
            emi = d["emi"]
            tax = d["tax"]
            exp = d["other_exp"]
            # calculating monthly expenses and income from existing data
            expenses_monthly = emi + tax + exp
            income_monthly = rent - expenses_monthly
            dt = Data(
                name=name,
                price=price,
                rent=rent,
                emi=emi,
                tax=tax,
                exp=exp,
                # adding new values to data
                expenses_monthly=expenses_monthly,
                income_monthly=income_monthly,
            )
            # saving object
            dt.save()
        # getting all data
        data_objects = Data.objects.all()
        # setting data as context
        context = {"data_objects": data_objects}
        # returning data in views
        return render(request, "myapp/index.html", context)
    else:
        print("This is a GET request")
    return render(request, "myapp/index.html")
