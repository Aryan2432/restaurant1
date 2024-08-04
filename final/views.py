from django.shortcuts import render
from book.models import one
def front(request):
    return render(request,"front.html")
def about(request):
    return render(request,"about.html")
def chefs(request):
    return render(request,"chefs.html")
def menu(request):
    return render(request,"menu.html")
def contact(request):
    return render(request,"contact.html")
def index(request):
    if request.method=="POST":
        a1=request.POST.get("a1")
        a2=request.POST.get("a2")
        a3=request.POST.get("a3")
        a4=request.POST.get("a4")
        a5=request.POST.get("a5")
        a6=request.POST.get("a6")
        a=one(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6)
        a.save()
    return render(request,"index.html")
def header(request):
    return render(request,"header.html")