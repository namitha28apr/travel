from django.shortcuts import render
from django.shortcuts import render
from . models import place,character


def input(request):
    obj=place.objects.all()
    obj1=character.objects.all()

    return render(request,"index.html",{'result':obj,'result1':obj1})
