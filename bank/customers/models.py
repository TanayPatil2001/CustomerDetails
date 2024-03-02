from django.db import models

# Create your models here.
class customersDetailsModel(models.Model):
    Age = models.IntegerField()
    Balance = models.IntegerField(default=None)
    Campaign = models.IntegerField(default=None)
    Contact = models.BigIntegerField(default=None)
    job = [('admin','admin'),('blue-collar','blue-collar'),('entrepreneur','entrepreneur'),('housemaid','housemaid'),('management','management'),('retired','retired'),('self-employed','self-employed'),('services','services'),('student','student'),('technician','technician'),('unemployed','unemployed'),('unknown','unknown')]
    Job = models.CharField(max_length=20,choices=job,default='unknown')
    Day = models.IntegerField(default=None)
    #Default = models.CharField(max_length=10)
    Duration = models.IntegerField(default=None)
    housing = [('yes','yes'),('no','no')]
    Housing = models.CharField(max_length=10,choices=housing,default=None)
    loan = [('yes','yes'),('no','no')]
    Loan = models.CharField(max_length=10,choices=loan,default=None)
    Marital = [('Married','Married'),('Single','Single'),('Divorced','Divorced')]
    Marital = models.CharField(max_length=10,choices=Marital,default='Single')
    Education = [('primary','primary'),('secondary','secondary'),('tertiary','tertiary'),('unknown','unknown')]
    Education = models.CharField(max_length=10,choices=Education,default='unknown')
    month = [('Jan','Jan'),('Feb','Feb'),('Mar','Mar'),('Apr','Apr'),('May',"May"),('Jun','Jun'),('July','July'),('Aug','Aug'),('Sept','Sept'),('Oct','Oct'),('Nov','Nov'),('Dec','Dec')]
    Month = models.CharField(max_length=10,choices=month,default=None)
    pdays = models.IntegerField(default=None)
    poutcome = [('Success','Success'),('Failure','Failure'),('Other','Other'),('Unknown','Unknown')]
    poutcome = models.CharField(max_length=10,choices=poutcome,default='Unknown')
    previous = models.IntegerField(default=None)







