from django.db import models


# Create your models here.
class PetListing(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    fixed = models.CharField(max_length=50)
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


class ItemListing(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=500)
    condition = models.CharField(max_length=500)
    animal = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    pictures = models.CharField(max_length=50)
    user = models.ForeignKey('User', default=None, null=True, on_delete=models.CASCADE)

    def __int__(self):
        return self.name


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __int__(self):
        return self.username


class Lost(models.Model):
    name = models.CharField(max_length=50)
    lastSeen = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pictures = models.CharField(max_length=50)
    user = models.ForeignKey('User', default=None, null=True, on_delete=models.CASCADE)

    def __int__(self):
        return self.name
