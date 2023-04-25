from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.Userlogin,name="login"),
    path('register/',views.UserRegistration,name="register")
]
