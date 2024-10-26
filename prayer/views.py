from django.shortcuts import render

def index(request):
    name = "Nathon"
    return render(request, "prayer/index.html", {"name":name} )
