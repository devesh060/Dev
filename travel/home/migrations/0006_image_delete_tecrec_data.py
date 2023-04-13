# Generated by Django 4.1.7 on 2023-04-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_tecrec_data_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("photo", models.ImageField(upload_to="myimage")),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="tecRec_data",
        ),
    ]
