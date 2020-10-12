from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world !")


# def runoob(request):
#     context ={}
#     context['hello'] = "Hello World!"
#     context['demo'] = '测试通过！'
#     return render(request,'runoob.html',context)

def runoob(request):
    views_name = ['runoob1','runoob2','runoob3']
    return render(request,"runoob.html",{"name":views_name})