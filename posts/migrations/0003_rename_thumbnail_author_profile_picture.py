# Generated by Django 3.2 on 2021-04-29 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='thumbnail',
            new_name='profile_picture',
        ),
    ]
