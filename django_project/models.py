from django.db import models
from django.forms import ModelForm



class User(models.Model):
  email = models.EmailField(max_length = 254,blank=True,unique = True)
  username = models.CharField(max_length=45,unique = True)
  password = models.CharField(max_length=32)
  
  def __str__(self):
    return self.email + self.username + self.password 
  
class Gifts(models.Model):
  gift = models.CharField(max_length=32)
  username = models.ForeignKey(User,on_delete=models.CASCADE)
  def __str__(self):
    return self.gift 