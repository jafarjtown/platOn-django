from asyncore import read
from django.contrib import admin
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)

admin.site.register(Tutorial, TutorialAdmin)
