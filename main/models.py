from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_post = models.TextField(default='Write your post here...')
    image = models.ImageField(upload_to='post/', blank=True)
    video = models.FileField(upload_to='video/', blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}, '{self.status}, at {self.updated}"