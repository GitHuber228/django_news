# Generated by Django 3.1 on 2020-08-30 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20200830_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitemainsettingsmodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Site description'),
        ),
        migrations.AddField(
            model_name='sitemainsettingsmodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Site description'),
        ),
    ]