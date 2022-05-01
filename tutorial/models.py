from django.db import models
from django.template.defaultfilters import slugify


class Tutorial(models.Model):
    title = models.CharField(max_length=256)
    tutor = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True, related_name='tutorials')
    body = models.TextField()
    attached_files = models.OneToOneField("TutorialFiles", on_delete=models.SET_NULL, null=True , blank=True)
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.slug = slugify(self.title)
        return super(Tutorial, self).save(*args, **kwargs)
    
class TutorialFiles(models.Model):
    videos = models.ManyToManyField('File', blank=True, related_name='tutorial_videos')
    images = models.ManyToManyField('File', blank=True, related_name='tutorial_images')
    document = models.ManyToManyField('File', blank=True, related_name='tutorial_documents')
    

class File(models.Model):
    obj = models.FileField()
    created_on = models.DateTimeField(auto_now_add=True)