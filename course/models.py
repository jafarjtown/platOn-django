from pyexpat import model
from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    text = models.TextField()
    contents = models.ManyToManyField('CourseContent', blank=True)
    developer = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True)
    

class CourseContent(models.Model):
    file = models.FileField(upload_to='course')
    text = models.TextField()