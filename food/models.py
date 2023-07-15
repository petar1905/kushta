from django.db import models

class FoodDate(models.Model):
  date = models.DateField()
  lunch = models.CharField(max_length=60)
  dinner = models.CharField(max_length=60)

# Create your models here.
