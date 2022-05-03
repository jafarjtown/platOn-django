
from django.db import models
from django.template.defaultfilters import slugify
import datetime
# Create your models here.
   
class File(models.Model):
    obj = models.FileField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    

class Event(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    start = models.DateField(auto_now=False)
    ongoing = models.BooleanField(default=False)
    
    @property
    def is_expired(self):
        return self.start <= datetime.date.today()
    