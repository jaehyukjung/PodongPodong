# Generated by Django 2.2.20 on 2021-10-25 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_auto_20211025_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]