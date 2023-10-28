from django.db import models

class Region(models.Model):
  name = models.CharField(max_length=20)
  def __str__(self):
    return self.name

class Input(models.Model):
  time = models.DateTimeField()
  address = models.CharField(max_length=45)
  region = models.ForeignKey(Region,on_delete=models.CASCADE)
  day = models.CharField(max_length=15)
  def __str__(self):
    return str(self.time) + self.address + str(self.region) + str(self.day)