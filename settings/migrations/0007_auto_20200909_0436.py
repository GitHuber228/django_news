# Generated by Django 3.1 on 2020-09-09 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_sitemainsettingsmodel_deleted_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitemainsettingsmodel',
            name='deleted_avatar',
            field=models.ImageField(upload_to='images/settings', verbose_name='Deleted avatar'),
        ),
    ]
