# Generated by Django 4.0.2 on 2022-04-27 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0002_answer_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj', models.FileField(upload_to='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TutorialFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ManyToManyField(blank=True, related_name='tutorial_documents', to='community.File')),
                ('images', models.ManyToManyField(blank=True, related_name='tutorial_images', to='community.File')),
                ('videos', models.ManyToManyField(blank=True, related_name='tutorial_video', to='community.File')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('slug', models.SlugField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('attached_files', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='community.tutorialfiles')),
                ('tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tutorials', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
