# Generated by Django 4.2.7 on 2024-06-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DocumentFlow", "0006_file_rejection_notes"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="rejectionNote",
            field=models.TextField(blank=True),
        ),
    ]
