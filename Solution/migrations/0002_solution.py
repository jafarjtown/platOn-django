# Generated by Django 4.0.2 on 2022-05-01 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Solution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_img', models.ImageField(null=True, upload_to='cover_images')),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=500)),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('source', models.URLField()),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='helper.prolang')),
                ('solver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='solutions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]