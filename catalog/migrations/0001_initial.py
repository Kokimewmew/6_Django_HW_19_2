# Generated by Django 5.0.6 on 2024-05-21 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "title",
                    models.CharField(
                        help_text="Введите название категории",
                        max_length=100,
                        verbose_name="Наименование категории",
                    ),
                ),
                (
                    "desk",
                    models.TextField(
                        help_text="Введите описание категории",
                        verbose_name="Описание категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                    "title",
                    models.CharField(
                        help_text="Введите название продукта",
                        max_length=100,
                        verbose_name="Наименование продукта",
                    ),
                ),
                (
                    "desk",
                    models.CharField(
                        help_text="Введите описание продукта",
                        max_length=100,
                        verbose_name="Описание продукта",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение продукта",
                        null=True,
                        upload_to="product/photo",
                        verbose_name="Изображение(превью)",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        blank=True,
                        help_text="Введите Цену за покупку продукта",
                        null=True,
                        verbose_name="Цена за покупку",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        help_text="Введите Дату создания продукта",
                        verbose_name="Дата создания(записи в БД)",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        help_text="Введите Дату последнего изменения продукта",
                        verbose_name="Дата последнего изменения(записи в БД)",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите Категорию продукта",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["category", "title"],
            },
        ),
    ]
