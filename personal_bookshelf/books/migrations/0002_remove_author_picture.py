# Generated by Django 4.2.11 on 2024-10-02 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='picture',
        ),
    ]
