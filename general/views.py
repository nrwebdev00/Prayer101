from django.shortcuts import render

def index(request):
    context = {'test': 'nathon'}
    return render(request, "general/index.html",   context )
