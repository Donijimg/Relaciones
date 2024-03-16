from django.db import models

from datetime import date

# Create your models here.
class Place(models.Model):
  name=models.CharField(max_length=50)
  addres=models.CharField(max_length=80)


#  def __str__(self):
#    return self.
    
class Restaurant(models.Model):
  place=models.OneToOneField(
    Place,
    on_delete=models.CASCADE,
    primary_key=True,
  )

  employees= models.IntegerField(default=1)

  
#  def __str__(self):
#    return self.