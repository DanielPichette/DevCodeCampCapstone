from django.db import models


# Create your models here.
class PetListing(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    nature = models.CharField(max_length=50)
    spayed = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    children = models.CharField(max_length=50)
    pets = models.CharField(max_length=50)
    description = models.CharField(max_length=20000)
    pictures = models.CharField(max_length=50)
    user = models.CharField(max_length=50)

    def __int__(self):
        return self.name
