# Generated by Django 4.2.7 on 2024-06-14 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("DocumentFlow", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="assigned_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assigned_files",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="file",
            name="uploaded_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="uploaded_files",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
