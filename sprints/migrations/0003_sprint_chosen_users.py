# Generated by Django 5.1.1 on 2024-10-21 15:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sprints", "0002_sprint_users"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="sprint",
            name="chosen_users",
            field=models.ManyToManyField(
                blank=True, related_name="chosen_sprints", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]