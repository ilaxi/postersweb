# Generated by Django 5.0.2 on 2025-02-22 11:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_short_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
