from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Question(models.Model):
    questionier = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True, related_name='questions')
    title = models.CharField(max_length=250)
    body = models.TextField()
    answers = models.ManyToManyField('Answer', blank=True)
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.slug = slugify(self.title)
        return super(Question, self).save(*args, **kwargs)
    
class Answer(models.Model):
    answerer = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True, related_name='answers')
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
