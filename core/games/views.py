from django.shortcuts import render
import requests
import json 
# Create your views here.

url = 'https://www.mmobomb.com/api1/games'
r = requests.get(url)


def home(request):

    data = json.loads(r.text)
    # print(data)
    context = {'data':data}
    return render(request, 'games/home.html',context)