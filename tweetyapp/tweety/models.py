from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweety(models.Model):
    #name = models.CharField(max_length=200,null=True)
    tweeticerik = models.CharField(max_length=800,null=True)
    address = models.CharField(max_length=200,null=True)

    #def __str__(self):
        #return self.name

class Predicted_Tweets(models.Model):
    tweet=models.CharField(max_length=800,null=True)
    location=models.CharField(max_length=200,null=True)      

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    pwd = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username
    