from rest_framework import serializers
from .models import PetListing
from .models import ItemListing
from .models import User
from .models import Lost


class PetListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetListing
        fields = ['id', 'name', 'type', 'age', 'fixed', 'gender', 'breed', 'price', 'children', 'pets',
                  'description', 'pictures', 'user']


class ItemListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemListing
        fields = ['id', 'name', 'condition', 'animal', 'category', 'description', 'pictures', 'user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'username', 'email', 'state', 'city', 'address', 'zipcode', 'phone',
                  'password']


class LostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lost
        fields = ['id', 'name', 'lastSeen', 'description', 'phone', 'email', 'pictures', 'user']
