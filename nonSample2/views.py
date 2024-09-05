from django.shortcuts import render

def funcHelloWorld(request):
    return render(request, 'index.html')
