from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add-contact/', views.addContact, name='add-contact'),
    path('profile/<int:pk>', views.contactProfile, name='profile'),
    path('edit-contact/<int:pk>', views.editContact, name='edit-contact'),
    path('delete/<int:pk>', views.deleteContact, name='delete'),
]