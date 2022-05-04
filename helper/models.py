from django.db import models

class ProLang(models.Model):
    name = models.CharField(max_length=50)
    
class PubContent(models.Model):
    cover_img = models.ImageField(upload_to="uploads/cover_images/%Y/%m/%d/", null=True)
    content = models.TextField()
    title = models.CharField(max_length=32)
    summary = models.CharField(max_length=256)
    language = models.ForeignKey(ProLang, on_delete=models.PROTECT)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
    
    
    
