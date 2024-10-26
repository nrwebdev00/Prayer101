from django.urls import path

from prayer.views import Index

urlpatterns = [
    path("", Index.as_view(), name='prayers-index')
]