# Generated by Django 3.1.1 on 2020-12-31 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_blocks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blocks',
            new_name='places',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='dest',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='img',
            new_name='photo',
        ),
    ]
