# Generated by Django 3.0.3 on 2020-04-23 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='upload_image'),
        ),
    ]