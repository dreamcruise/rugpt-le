# Generated by Django 5.1.3 on 2024-11-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_useraccount_slug_privatekey"),
    ]

    operations = [
        migrations.AddField(
            model_name="privatekey",
            name="last_call",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
