#coding:utf-8
from django.shortcuts import render
from django.http import HttpRespones

# Create your views here.
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpRespones(str(c))
