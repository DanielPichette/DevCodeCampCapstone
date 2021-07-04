from django.urls import path
from . import views

urlpatterns = [
    #PETS
    path('Pets/', views.PetListings.as_view()),
    path('PetByID/<int:pk>/', views.PetListingById.as_view()),
    #Items
    path('Items/', views.ItemListings.as_view()),
    path('ItemById/<int:pk>/', views.ItemListingById.as_view()),
    #Users
    path('Users/', views.Users.as_view()),
    path('UserById/<int:pk>/', views.UserById.as_view()),
    #Lost Pets
    path('LostPets/', views.LostPets.as_view()),
    path('LostPetById/<int:pk>/', views.LostPetById.as_view()),

]
