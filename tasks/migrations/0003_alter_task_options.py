# Generated by Django 5.1.3 on 2024-12-03 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_rename_datetime_task_created_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["status", "-created_at"]},
        ),
    ]