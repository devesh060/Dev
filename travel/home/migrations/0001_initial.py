# Generated by Django 4.1.7 on 2023-03-13 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OpsPageInfo",
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
                (
                    "campaign_name",
                    models.CharField(blank=True, max_length=100, unique=True),
                ),
                ("campaign_pic", models.ImageField(upload_to="images/opspage_pics")),
                ("description_header", models.CharField(blank=True, max_length=100)),
                ("campaign_description", models.CharField(blank=True, max_length=600)),
                ("goal", models.CharField(blank=True, max_length=100)),
                ("perk_header1", models.CharField(blank=True, max_length=100)),
                ("perk_description1", models.CharField(blank=True, max_length=600)),
            ],
        ),
    ]