# Generated by Django 5.0.4 on 2024-07-09 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_recipescommments_recipescomments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipesComments',
            new_name='RecipeCommments',
        ),
        migrations.RenameField(
            model_name='recipecommments',
            old_name='recipesid',
            new_name='recipeid',
        ),
    ]
