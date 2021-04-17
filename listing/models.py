from django.db import models
from datetime import datetime
from django.conf import settings


class Lists(models.Model):
    TITLE=(
        ('Mr.','Mr.'),
        ('Miss.','Miss'),
        ('Dr.','Dr.'),
        ('Mrs.','Mrs.'),
        ('',''),
    )

    
    account_number = models.CharField(max_length=20,unique=True,blank=False) 
    title=models.CharField(max_length=6,choices=TITLE,null=True,blank=True)
    first_name=models.CharField(max_length=100,blank=True,null=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    job_title=models.CharField(max_length=75,null=True,blank=True)
    company_name=models.CharField(max_length=100,null=True,default='Company not entered.')
    address=models.CharField(max_length=150,null=True,blank=True)
    address1=models.CharField(max_length=150,null=True,blank=True)
    address2=models.CharField(max_length=150,null=True,blank=True)
    city=models.CharField(max_length=75,null=True,blank=True)
    state=models.CharField(max_length=20,null=True,blank=True)
    zip_code=models.CharField(max_length=30,null=True,blank=True)
    country=models.CharField(max_length=90,default='United States',null=True)
    email=models.EmailField(max_length=254,null=True,blank=True)
    phone_number=models.CharField(max_length=25,null=True, blank=True)
    date_updated=models.DateTimeField(auto_now=datetime.now, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.account_number
