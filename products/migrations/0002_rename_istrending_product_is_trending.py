# Generated by Django 3.2.25 on 2024-04-14 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='isTrending',
            new_name='is_trending',
        ),
    ]
