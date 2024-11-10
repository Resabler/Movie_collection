from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    name=models.CharField(max_length=200)
    user_username=models.CharField(max_length=100)
    description=models.CharField(max_length=150)
    def save(self,*args,**kwargs):
        try:
            super().save(*args, **kwargs)
        except:    
             if not User.objects.filter(username=self.user_username).exists():
              raise ValueError(f"User with username {self.user_username} does not exist.")
        

     

class Movie(models.Model):
    title=models.CharField(max_length=200)
    genre=models.CharField(max_length=100)
    collection=models.ForeignKey(Collection,on_delete=models.CASCADE)
    description=models.CharField(max_length=100)    

