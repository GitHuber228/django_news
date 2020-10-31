# Generated by Django 3.1.2 on 2020-10-31 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import libs.utils
import libs.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=18, unique=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=18, null=True, unique=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=18, null=True, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, help_text='Write nothing if you want to set slug field automatically', unique=True, verbose_name='Slug')),
                ('image', models.ImageField(blank=True, help_text='Must be 1920x480px', upload_to=libs.utils.get_category_upload_path, validators=[libs.validators.validate_category_tag_image], verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=255, null=True, unique=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, null=True, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, help_text='Write nothing if you want to set slug field automatically', max_length=255, unique=True, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Content')),
                ('content_ru', models.TextField(null=True, verbose_name='Content')),
                ('content_en', models.TextField(null=True, verbose_name='Content')),
                ('header_image', models.ImageField(help_text='Must be 1920x720px', upload_to=libs.utils.get_post_upload_path, validators=[libs.validators.validate_header_image], verbose_name='Header image')),
                ('post_image', models.ImageField(help_text='Must be 1200x800px', upload_to=libs.utils.get_post_upload_path, validators=[libs.validators.validate_post_image], verbose_name='Post image')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Views')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published')),
                ('once_published', models.BooleanField(default=False, verbose_name='Once published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post_category', to='news.postcategorymodel', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PostTagModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=18, unique=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=18, null=True, unique=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=18, null=True, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, help_text='Write nothing if you want to set slug field automatically', unique=True, verbose_name='Slug')),
                ('image', models.ImageField(blank=True, help_text='Must be 1920x480px', upload_to=libs.utils.get_tag_upload_path, validators=[libs.validators.validate_category_tag_image], verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PostViewsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.postmodel', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Post views',
                'verbose_name_plural': 'Post views',
            },
        ),
        migrations.AddField(
            model_name='postmodel',
            name='tags',
            field=models.ManyToManyField(related_name='post_tags', to='news.PostTagModel', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='PinnedPostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pinned_post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pinned_posts', to='news.postmodel', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Pinned post',
                'verbose_name_plural': 'Pinned posts',
                'ordering': ['-pinned_post__created_at'],
            },
        ),
    ]
