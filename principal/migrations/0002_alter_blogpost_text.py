# Generated by Django 3.2.23 on 2024-01-20 13:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='text'),
        ),
    ]
