from django.db import models
from datetime import datetime

class Todo_List(models.Model):
    new_todo=models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=datetime.now)

    def __str__(self):
        return self.new_todo 
