from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

  
class Gifts(models.Model):
  gift = models.CharField(max_length=128)
  username = models.ForeignKey(User,on_delete=models.CASCADE)
  def __str__(self):
    return self.gift 