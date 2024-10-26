from django.urls import path

from general.views import Index

urlpatterns = [
    path("", Index.as_view(), name="general-index")
]