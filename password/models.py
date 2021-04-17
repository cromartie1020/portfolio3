from django.db import models
from django.utils import timezone
from django.conf import settings
class Word(models.Model):
    
    website=models.CharField(max_length=250,blank =True)
    pass_word = models.CharField(max_length=250,blank = True)
    user_name = models.CharField(max_length=250,blank= True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.website