# Generated by Django 5.1.1 on 2024-10-31 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_remove_task_assigned_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="estimation_ended",
            field=models.BooleanField(default=False),
        ),
    ]
