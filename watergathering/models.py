from django.db import models

class WaterGatherDate(models.Model):
  date = models.DateField()
  gatherer = models.CharField(max_length=60)
  completion = models.BooleanField()

# Create your models here.
