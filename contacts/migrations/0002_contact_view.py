# Generated by Django 3.2.8 on 2021-10-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='view',
            field=models.BooleanField(default=True),
        ),
    ]