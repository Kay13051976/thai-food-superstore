from django.db import models

# Create your models here.


class RecipesComments(models.Model):

    recipesid = models.CharField(max_length=50)
    username = models.CharField(max_length=150)
    comment = models.TextField()

    def __str__(self):
        return self.recipesid
