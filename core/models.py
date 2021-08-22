from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', primary_key=True)
    profile_image = models.ImageField(upload_to='media', default='media/default_image.jpg')
    bio = models.TextField(max_length=400, null=True, blank=True)
    
    @receiver(post_save, sender=User) 
    def create_user_profile(sender, instance, created, **kwargs):
	    if created:
		    Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
	    instance.profile.save()


    def __str__(self):
        return f"{self.user}"

class Snippet(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippets')
    code = models.TextField()
    language = models.CharField(max_length=30)
    created_at = DateTimeField(auto_now_add=True)
    copied = models.IntegerField(default=0)
    public = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'