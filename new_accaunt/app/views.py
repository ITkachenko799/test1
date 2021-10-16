from django.shortcuts import render
from .forms import *
from django.conf import settings

def handle_post(form,request):
    body={**request.POST}
    print(body)
    del body['csrfmiddlewaretoken']
    result=[]

    for field in body:
        result.append({'label': form[field].label, 'value':body[field][0]})
    return result

def task1(request):
    form = AccauntUser()
    response = None
    if request.method == "POST":
        response = handle_post(form,request)

    return render(request,"task1.html",{'form':form,'title':'Ratting','response':response})


def task2(request):
    form = Book()
    response = None
    if request.method == "POST":
        response = handle_post(form,request)

    return render(request,"task2.html",{'form':form,'title':'Ratting Book','response':response})