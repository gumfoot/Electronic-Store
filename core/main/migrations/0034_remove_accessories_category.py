# Generated by Django 5.0.6 on 2024-07-28 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_accessories_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessories',
            name='category',
        ),
    ]