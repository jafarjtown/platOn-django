
from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Article(models.Model):
    publisher = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True, related_name='articles')
    title = models.CharField(max_length=250)
    body = models.TextField()
    publish = models.BooleanField(default=False)
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)
    
    
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
    

class Tutorial(models.Model):
    tutor = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True, related_name='tutorials')
    title = models.CharField(max_length=250)
    body = models.TextField()
    attached_files = models.OneToOneField("TutorialFiles", on_delete=models.SET_NULL, null=True , blank=True)
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.slug = slugify(self.title)
        return super(Tutorial, self).save(*args, **kwargs)
    
class TutorialFiles(models.Model):
    videos = models.ManyToManyField('File', blank=True, related_name='tutorial_video')
    images = models.ManyToManyField('File', blank=True, related_name='tutorial_images')
    document = models.ManyToManyField('File', blank=True, related_name='tutorial_documents')
    

class File(models.Model):
    obj = models.FileField()
    created_on = models.DateTimeField(auto_now_add=True)
    