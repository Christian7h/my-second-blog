# Generated by Django 3.2.23 on 2024-01-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_carouselimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimage',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
