# Generated by Django 4.1.1 on 2022-10-20 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_social_youtube_profile_social_linkedin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='bdescription',
            new_name='description',
        ),
    ]
