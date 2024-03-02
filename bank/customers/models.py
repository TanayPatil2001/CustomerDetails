from django.db import models

# Create your models here.
class customersDetailsModel(models.Model):
    Age = models.IntegerField()
    Job = models.CharField(max_length=10)
    Marital = [('Married','Married'),('Single','Single'),('Divorced','Divorced')]
    Marital = models.CharField(max_length=10,choices=Marital,default='Single')
    Education = [('primary','primary'),('secondary','secondary'),('tertiary','tertiary'),('unknown','unknown')]
    Education = models.CharField(max_length=10,choices=Education,default='unknown')