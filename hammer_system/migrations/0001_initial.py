# Generated by Django 4.2.4 on 2023-08-17 06:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone_number", models.CharField(max_length=20)),
                ("authorization_code", models.CharField(max_length=4)),
                ("invite_code", models.CharField(max_length=6)),
                (
                    "activated_invite_code",
                    models.CharField(blank=True, max_length=6, null=True),
                ),
            ],
        ),
    ]
