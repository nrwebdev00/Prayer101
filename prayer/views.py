import os
from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv

# Load dot env files 
load_dotenv()



def index(request):
    name = "Nathon"
    return render(request, "prayer/index.html", {"name":name} )
