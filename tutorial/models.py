from tokenize import blank_re
from django.db import models
from django.template.defaultfilters import slugify
from account.models import User


class Tutorial(models.Model):

    BEGINNER = "BG"
    INTERMEDIATE = "IT"
    ADVANCED = "AD"
    LEVEL_CHOICES = [
        (BEGINNER, "Beginner"),
        (INTERMEDIATE, "Intermediate"),
        (ADVANCED, "Advanced"),
    ]

    BASH = "BH"
    C_C_PLUSPLUS = "CC"
    DART = "DT"
    GO = "GO"
    JAVA = "JV"
    JAVASCRIPT = "JS"
    KOTLIN = "KL"
    OBJECTIVE_C = "OC"
    PHP = "PP"
    PYTHON = "PY"
    SWIFT = "SW"
    PROGRAMMING_LANG_CHOICES = [
        (BASH, "Bash"),
        (C_C_PLUSPLUS, "C/C++"),
        (DART, "Dart"),
        (GO, "Go"),
        (JAVA, "Java"),
        (JAVASCRIPT, "JavaScript"),
        (KOTLIN, "Kotlin"),
        (OBJECTIVE_C, "Objective-C"),
        (PHP, "PHP"),
        (PYTHON, "Python"),
        (SWIFT, "Swift"),
    ]

    ENGLISH = "EN"
    FRENCH = "FR"
    LANGUAGE_CHOICES = [
        (ENGLISH, "English"),
        (FRENCH, "French"),
    ]

    cover_image = models.ImageField(upload_to="uploads/tutorial/cover_images/%Y/%m/%d/", blank=True)

    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    time_to_complete = models.IntegerField()

    main_lang = models.CharField(max_length=2, choices=PROGRAMMING_LANG_CHOICES)
    add_lang = models.CharField(max_length=2, choices=PROGRAMMING_LANG_CHOICES, blank=True)

    title = models.CharField(max_length=256)
    tutor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tutorials')
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    summary = models.CharField(max_length=256)
    overview = models.TextField()
    requirements = models.TextField()
    background = models.TextField()
    steps = models.TextField()
    
    # slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    # def save(self, *args, **kwargs) -> None:
    #     if not self.id:
    #         self.slug = slugify(self.title)
    #     return super(Tutorial, self).save(*args, **kwargs)
    