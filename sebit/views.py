# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
# from . import serializers
import requests, json
from . import service

from django.http import JsonResponse
# Create your views here.


def home(request):
    r=requests.get("https://api.myjson.com/bins/xa6vm")
    print(r.text)
    data=service.get("sadsdadsa")
    return render(request,'index.html',{'items':data})


def post(request,name,city,country):
            payload={
            "person_name": name,
            "city_name": city,
            "country_name": country
            }
            r=requests.post("https://api.myjson.com/bins",json=payload)
            x=r.text
            d=json.loads(x)
            print(d['uri'])
            return JsonResponse(d,safe=False)



def put(request):
    data=service.get("https://api.myjson.com/bins/xa6vm")

    add_data = 	{
        "person_name": "person_name",
        "city_name": "city_name",
        "country_name": country
    	}

    data.append(add_data)


    r=requests.put("https://api.myjson.com/bins/x0482",json=data)
    print(r.content)

    return render(request,'index.html')
