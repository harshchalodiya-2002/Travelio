# Generated by Django 3.1.1 on 2020-10-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201015_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='blocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('dest', models.CharField(max_length=50)),
            ],
        ),
    ]
