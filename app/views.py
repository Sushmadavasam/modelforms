from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_Topic(request):
    TMF=TopicModelForm()
    d={'TMF':TMF}
    if request.method=='POST':
        TMFO=TopicModelForm(request.POST)
        if TMFO.is_valid:
            TMFO.save()
        return HttpResponse('data is submitted')
    return render(request,'insert_Topic.html',d)

def insert_Webpage(request):
    WMF=WebpageModelForm()
    d={'WMF':WMF}
    if request.method=='POST':
        WMFO=WebpageModelForm(request.POST)
        if WMFO.is_valid:
            WMFO.save()
        return HttpResponse('WEBPAGE submitted')
    return render(request,'insert_Webpage.html',d)