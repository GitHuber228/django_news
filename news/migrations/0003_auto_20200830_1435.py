# Generated by Django 3.1 on 2020-08-30 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200829_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcategorymodel',
            name='title_en',
            field=models.CharField(max_length=18, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='postcategorymodel',
            name='title_ru',
            field=models.CharField(max_length=18, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title_en',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='posttagmodel',
            name='title_en',
            field=models.CharField(max_length=18, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='posttagmodel',
            name='title_ru',
            field=models.CharField(max_length=18, null=True, unique=True, verbose_name='Title'),
        ),
    ]
