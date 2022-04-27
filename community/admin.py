from django.contrib import admin

from community.models import Answer, Article, Question, Tutorial

# Register your models here.


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Article)
admin.site.register(Tutorial)