from django.shortcuts import render

# Create your views here.
def deshboard(request):
    return render (request, 'deshboard/deshboard.html')