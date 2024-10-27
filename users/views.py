from django.shortcuts import render
from django.views import View

class Profiles(View):
    def get(self, request):
        context = {}
        return render(request, "users/profiles.html", context)
