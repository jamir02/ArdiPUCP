# Generated by Django 4.1.3 on 2022-11-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="usuario",
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
                ("nombre", models.CharField(default="", max_length=64)),
                ("local", models.CharField(default="", max_length=64)),
                ("codigo_usuario", models.CharField(default="", max_length=64)),
                ("clave", models.CharField(default="", max_length=64)),
            ],
        ),
    ]
