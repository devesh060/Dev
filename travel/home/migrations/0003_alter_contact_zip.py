# Generated by Django 4.1.7 on 2023-03-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_contact_alter_opspageinfo_campaign_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="zip",
            field=models.IntegerField(),
        ),
    ]