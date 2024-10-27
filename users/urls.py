from django.urls import path

from users.views import Profiles

urlpatterns = [
    path("profiles/", Profiles.as_view(), name='users-profiles'),
]