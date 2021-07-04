from django.db import models


# Create your models here.
class PetListing(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    fixed = models.BooleanField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    breed = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    children = models.BooleanField(null=True, blank=True)
    pets = models.BooleanField(null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    pictures = models.ImageField(null=True, blank=True, upload_to="images/")
    user = models.ForeignKey('User', default=None, null=True, on_delete=models.CASCADE)

    def __int__(self):
        return self.name


class ItemListing(models.Model):
    name = models.CharField(max_length=50)
    condition = models.CharField(max_length=500, null=True, blank=True)
    animal = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    pictures = models.ImageField(null=True, blank=True, upload_to="images/")
    user = models.ForeignKey('User', default=None, null=True, on_delete=models.CASCADE)

    def __int__(self):
        return self.name


class User(models.Model):
    firstName = models.CharField(max_length=50, )
    lastName = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    state = models.CharField(max_length=50, default=None, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50)

    def __int__(self):
        return self.username


class Lost(models.Model):
    name = models.CharField(max_length=50)
    lastSeen = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    pictures = models.ImageField(null=True, blank=True, upload_to="images/")
    user = models.ForeignKey('User', default=None, null=True, on_delete=models.CASCADE)

    def __int__(self):
        return self.name
