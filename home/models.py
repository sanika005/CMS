from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="Email Address",max_length=255,unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class PostModel(models.Model):
    user = models.ForeignKey("UserModel",on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class LikeModel(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post_id','user_id')

    def __str__(self):
        return f'{self.user} likes {self.post}'