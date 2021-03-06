# Generated by Django 4.0.2 on 2022-05-03 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_remove_article_publisher_remove_question_answers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('start', models.DateField(auto_now=True)),
                ('ongoing', models.BooleanField(default=False)),
            ],
        ),
    ]
