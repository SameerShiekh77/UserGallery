
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('change-password/', views.change_password, name='chnage-password'),
    path('forget-password/', views.forget_password, name='forget-password'),

]
