from django.contrib import admin
from .models import PetListing
from .models import ItemListing
from .models import User
from .models import Lost

# Register your models here.
admin.site.register(PetListing)
admin.site.register(ItemListing)
admin.site.register(User)
admin.site.register(Lost)
