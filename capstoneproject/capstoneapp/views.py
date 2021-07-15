from django.shortcuts import render

from django.http import Http404
from .models import PetListing
from .models import ItemListing
from .models import User
from .models import Lost
from .serializers import PetListingSerializer
from .serializers import ItemListingSerializer
from .serializers import UserSerializer
from .serializers import LostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
# ----------------------------PET LISTING ---------------------------------
# ---ALL---------------------------
class PetListings(APIView):

    def get(self, request):
        listings = PetListing.objects.all()
        serializer = PetListingSerializer(listings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PetListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---BY ID------------------------
class PetListingById(APIView):
    def get_object(self, pk):
        try:
            return PetListing.objects.get(pk=pk)
        except PetListing.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        listing = self.get_object(pk)
        serializer = PetListingSerializer(listing)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        listing = self.get_object(pk)
        serializer = PetListingSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        listing = self.get_object(pk)
        listing.delete()
        return Response(status=status.HTTP_200_OK)


# ----------------------------ITEM LISTING ---------------------------------
# ---ALL---------------------------
class ItemListings(APIView):

    def get(self, request):
        listings = ItemListing.objects.all()
        serializer = ItemListingSerializer(listings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---BY ID------------------------
class ItemListingById(APIView):
    def get_object(self, pk):
        try:
            return ItemListing.objects.get(pk=pk)
        except ItemListing.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        listing = self.get_object(pk)
        serializer = ItemListingSerializer(listing)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        listing = self.get_object(pk)
        serializer = ItemListingSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        listing = self.get_object(pk)
        listing.delete()
        return Response(status=status.HTTP_200_OK)


# -----------------------------------USER -----------------------------------
# ---ALL---------------------------
class Users(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---BY ID------------------------
class UserById(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        updateUser = self.get_object(pk)
        serializer = UserSerializer(updateUser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_200_OK)


# -----------------------------------Lost Pet-----------------------------------
# ---ALL---------------------------
class LostPets(APIView):

    def get(self, request):
        pets = Lost.objects.all()
        serializer = LostSerializer(pets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---BY ID------------------------
class LostPetById(APIView):
    def get_object(self, pk):
        try:
            return Lost.objects.get(pk=pk)
        except Lost.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pet = self.get_object(pk)
        serializer = LostSerializer(pet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        updateLostPet = self.get_object(pk)
        serializer = LostSerializer(updateLostPet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        lostPetListing = self.get_object(pk)
        lostPetListing.delete()
        return Response(status=status.HTTP_200_OK)
