from django.db import models


class MyUser(models.Model):
  username = models.CharField(max_length=128)
  password = models.CharField(max_length=128)

class Gifts(models.Model):
  gift = models.CharField(max_length=128)
  username = models.ForeignKey(MyUser,on_delete=models.CASCADE)
  def __str__(self):
    return self.gift 

