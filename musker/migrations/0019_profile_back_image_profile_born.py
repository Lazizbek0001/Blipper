# Generated by Django 5.0.4 on 2024-07-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0018_alter_comment_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='back_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='born',
            field=models.DateTimeField(default=None),
        ),
    ]
