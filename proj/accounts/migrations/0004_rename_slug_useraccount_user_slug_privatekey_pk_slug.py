# Generated by Django 5.1.3 on 2024-11-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_privatekey_last_call"),
    ]

    operations = [
        migrations.RenameField(
            model_name="useraccount",
            old_name="slug",
            new_name="user_slug",
        ),
        migrations.AddField(
            model_name="privatekey",
            name="pk_slug",
            field=models.SlugField(default=""),
        ),
    ]
