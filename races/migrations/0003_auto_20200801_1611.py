# Generated by Django 3.0.8 on 2020-08-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0002_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='race',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]