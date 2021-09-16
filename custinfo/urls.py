from django.urls import path
from . import views



urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('clogin/', views.clogin, name='login'),
    path('cprofile/', views.cprofile, name='profile'),
    path('clogout/', views.clogout, name='logout'),
]