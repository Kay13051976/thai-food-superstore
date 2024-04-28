from django.db import models

# Create your models here.
class RecipeCommments(models.Model):

    recipeid = models.CharField(max_length=50)
    username = models.CharField(max_length=150)
    comment = models.TextField()

    def __str__(self):
        return self.recipeid