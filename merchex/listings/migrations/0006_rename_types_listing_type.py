# Generated by Django 5.0.1 on 2024-01-27 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_listing_description_listing_sold_listing_types_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='types',
            new_name='type',
        ),
    ]