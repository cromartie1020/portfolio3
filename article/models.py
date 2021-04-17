from django.db import models
from django.conf import settings
from datetime import datetime
class Article(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    head_line=models.CharField(max_length=75,null=True)
    body=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=datetime.now)
    created=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return head_line



