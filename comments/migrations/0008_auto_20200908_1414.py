# Generated by Django 3.1 on 2020-09-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_auto_20200908_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcommentmodel',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
    ]