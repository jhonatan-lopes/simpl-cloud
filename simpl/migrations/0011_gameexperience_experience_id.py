# Generated by Django 3.2 on 2021-08-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("simpl", "0010_class"),
    ]

    operations = [
        migrations.AddField(
            model_name="gameexperience",
            name="experience_id",
            field=models.UUIDField(blank=True, db_index=True, null=True),
        ),
    ]
