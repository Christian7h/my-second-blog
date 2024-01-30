# Generated by Django 5.0.1 on 2024-01-30 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0010_reservacita'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleCalendarButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('color', models.CharField(max_length=7)),
            ],
        ),
    ]
