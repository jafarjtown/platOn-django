# Generated by Django 4.0.2 on 2022-05-01 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0001_initial'),
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='helper.prolang'),
        ),
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
