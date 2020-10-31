# Generated by Django 3.1.2 on 2020-10-31 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSubscriptionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Email subscription',
                'verbose_name_plural': 'Email subscriptions',
            },
        ),
        migrations.CreateModel(
            name='MailUsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('question_subject', models.CharField(max_length=255, verbose_name='Mail subject')),
                ('question_message', models.TextField(verbose_name='Mail message')),
                ('answer_subject', models.CharField(blank=True, max_length=255, verbose_name='Answer mail subject')),
                ('answer_message', models.TextField(blank=True, verbose_name='Answer mail message')),
                ('answer_staff', models.CharField(blank=True, max_length=150, verbose_name='Answer staff')),
                ('is_answered', models.BooleanField(blank=True, default=False, verbose_name='Is answered')),
            ],
            options={
                'verbose_name': 'Mail letter',
                'verbose_name_plural': 'Mail letters',
                'ordering': ['-id'],
            },
        ),
    ]
