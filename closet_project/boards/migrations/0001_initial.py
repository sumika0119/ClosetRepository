# Generated by Django 4.2.7 on 2024-02-04 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categories",
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
                ("category_name", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "categories",
            },
        ),
        migrations.CreateModel(
            name="Clothe_Colors",
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
            ],
        ),
        migrations.CreateModel(
            name="Colors",
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
                ("color_name", models.CharField(max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "colors",
            },
        ),
        migrations.CreateModel(
            name="Clothes",
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
                ("title", models.CharField(max_length=255)),
                (
                    "picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="closet_project/media/"
                    ),
                ),
                ("price", models.IntegerField(blank=True, default=0, null=True)),
                ("purchase_date", models.DateField(blank=True, null=True)),
                ("store", models.CharField(default="", max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="boards.categories",
                    ),
                ),
                (
                    "color",
                    models.ManyToManyField(
                        blank=True,
                        related_name="clothe",
                        through="boards.Clothe_Colors",
                        to="boards.colors",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "clothes",
            },
        ),
        migrations.AddField(
            model_name="clothe_colors",
            name="clothe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="clothe_color_relation",
                to="boards.clothes",
            ),
        ),
        migrations.AddField(
            model_name="clothe_colors",
            name="color",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="color_clothe_relation",
                to="boards.colors",
            ),
        ),
    ]
