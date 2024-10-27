from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("general.urls")),
    path('users/', include("users.urls")),
    path('prayer/', include("prayer.urls")),
    path('prayers/',include("prayer.urls")),
    path('admin/', admin.site.urls),
]
