# Generated by Django 4.2.2 on 2024-06-27 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank='True', max_length=100, null='True', verbose_name='Token'),
            preserve_default='True',
        ),
    ]
