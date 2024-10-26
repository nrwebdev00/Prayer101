from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        context = {'test':'nathon'}
        return render(request, "general/index.html", context )
