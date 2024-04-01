from django.db import models

# Create your models here.
class PlayerModel(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    ContactNumber = models.BigIntegerField()
    City = models.CharField(max_length=10)
