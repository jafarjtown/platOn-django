from django.db import models

class ProLang(models.Model):
    name = models.CharField(max_length=50)
    
class PubContent(models.Model):
    cover_img = models.ImageField(upload_to='cover_images', null=True)
    content = models.TextField()
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)
    language = models.ForeignKey(ProLang, on_delete=models.PROTECT, null=True)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
    
    
    
