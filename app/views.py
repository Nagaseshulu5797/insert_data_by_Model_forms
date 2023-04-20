from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Topic insertion ia successfully')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WFD=WebpageForm(request.POST)
        if WFD.is_valid():
            WFD.save()

            return HttpResponse('insertion of insert_webpage is successfully')
    return render(request,'insert_webpage.html',d)



def insert_access(request):
    ARF=AccessRecordForm()
    d={'ARF':ARF}
    if request.method=='POST':
        ARD=AccessRecordForm(request.POST)
        if ARD.is_valid():
            ARD.save()

            return HttpResponse('insert_access data is successfully')
    return render(request,'insert_access.html',d)


















