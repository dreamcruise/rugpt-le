# Generated by Django 5.1.3 on 2024-12-01 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_alter_privatekey_status_from_api"),
    ]

    operations = [
        migrations.AlterField(
            model_name="privatekey",
            name="status_from_api",
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
    ]
