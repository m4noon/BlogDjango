# Generated by Django 4.0.5 on 2022-06-25 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]