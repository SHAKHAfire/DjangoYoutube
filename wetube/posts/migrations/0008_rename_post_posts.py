# Generated by Django 5.0.1 on 2024-04-19 15:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_alter_postcomment_post_delete_posts'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Posts',
        ),
    ]
