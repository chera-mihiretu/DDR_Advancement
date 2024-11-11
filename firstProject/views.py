from django.http import HttpResponse 

def hellow(request):
    return HttpResponse("Hello World")