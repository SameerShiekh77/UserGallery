
from django.urls import path
from . import views

urlpatterns = [
    path('images/', views.upload_image, name='images'),
    path('delete/<int:id>', views.delete, name='delete'),

]
