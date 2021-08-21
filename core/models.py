from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField

# Create your models here.


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', primary_key=True)
    profile_image = models.ImageField(upload_to='profile', default="default_image.jpg")
    bio = models.TextField(max_length=400, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user}"

class Snippet(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippet')
    code = models.TextField()
    language = models.CharField(max_length=30)
    created_at = DateTimeField(auto_now_add=True)
    copied = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'