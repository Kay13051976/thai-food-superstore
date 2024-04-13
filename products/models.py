from django.db import models


class Product(models.Model):
    AVAILABILITY_CHOICES = [
        (0, 'NO'),
        (1, 'YES'),
    ]
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    isTrending = models.BooleanField(default=False)
    availability = models.SmallIntegerField(choices=AVAILABILITY_CHOICES, default=1)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
def __str__(self) -> str:
    return self.name