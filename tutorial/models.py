from django.db import models
from django.template.defaultfilters import slugify
from account.models import User


class Tutorial(models.Model):

    cover_image = models.ImageField(upload_to="uploads/tutorial/cover_images/%Y/%m/%d/", blank=True)

    level = models.CharField(max_length=32)
    time_to_complete = models.IntegerField()

    main_lang = models.CharField(max_length=32)
    add_lang = models.CharField(max_length=32, blank=True)

    title = models.CharField(max_length=256)
    tutor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tutorials')
    language = models.CharField(max_length=32)
    summary = models.CharField(max_length=256)
    overview = models.TextField()
    requirements = models.TextField()
    background = models.TextField()
    steps = models.TextField()
    
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.slug = slugify(self.title)
        return super(Tutorial, self).save(*args, **kwargs)
    