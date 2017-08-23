from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
        ('hiking', 'hiking'),
        ('trip', 'trip'),
        ('car', 'car')
)

class Route(models.Model):
    name = models.CharField(max_length=200)
    source = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES,
                                default='hiking',
                                max_length=100)

    def __str__(self):
        return self.name
