# Generated by Django 4.1.1 on 2022-09-26 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_slug_post_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='url',
            new_name='oid',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='url',
            new_name='oid',
        ),
    ]