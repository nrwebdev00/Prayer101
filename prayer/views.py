from django.shortcuts import render

from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        context = {'name': 'Nathon', 'date':'5-25-24'}
        return render(request, "prayer/index.html", context)