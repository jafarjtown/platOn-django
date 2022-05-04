from helper.models import PubContent
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Article(PubContent):
    publisher = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='articles')
    publish = models.BooleanField(default=False)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)
    
    
 