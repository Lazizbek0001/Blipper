# Generated by Django 5.0.4 on 2024-07-09 16:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0014_comment_likes_notification_post_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='Notifications',
        ),
    ]
