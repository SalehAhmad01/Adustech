
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', default='default-pic.jpeg')
    nickname = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    interests = models.ManyToManyField('Interest', blank=True)  # Many-to-Many relationship for tags
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)
    youtube = models.URLField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
