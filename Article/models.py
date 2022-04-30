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
    
    
 