import uuid
from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profile_image/', default='profile_image/default_image.png')
    country = models.CharField(max_length=100, default="USA")
    social_facebook = models.CharField(max_length=256, default="www.facebook.com")
    social_youtube = models.CharField(max_length=256, default="www.youtube.com")
    home_church = models.CharField(max_length=256, blank=True, null=True)
    home_mission = models.CharField(max_length=256, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.user.username)