# Generated by Django 3.1 on 2020-09-05 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200902_1247'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usermodel',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Last name'),
        ),
    ]
