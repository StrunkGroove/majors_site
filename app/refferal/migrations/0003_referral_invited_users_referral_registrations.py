# Generated by Django 4.2.5 on 2023-12-24 23:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('refferal', '0002_referral_clicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='invited_users',
            field=models.ManyToManyField(blank=True, related_name='invited_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='referral',
            name='registrations',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
