# Generated by Django 3.1.4 on 2021-03-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='participants',
            field=models.CharField(default='killer', max_length=1000),
        ),
    ]
