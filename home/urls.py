from django.urls import path ,include
from . import views
urlpatterns = [ 
    path('', views.index),
    path('contact/', views.contact),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('allauth.urls')),
    path('register/', views.register, name="register"),
]
