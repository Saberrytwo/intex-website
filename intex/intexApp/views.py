from django.shortcuts import render

# Create your views here.

def prescriberPageView(request) :
    return render(request, 'intexApp/prescriber.html')

def drugPageView(request) :
    return render(request, 'intexApp/drug.html')
