# Generated by Django 3.2.3 on 2021-06-03 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Blog',
        ),
    ]