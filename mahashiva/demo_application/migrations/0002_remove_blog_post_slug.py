# Generated by Django 3.0.3 on 2020-04-14 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_post',
            name='slug',
        ),
    ]