from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'a':200,'b':190,'c':150}
    return render(request,'conditions.html',d)