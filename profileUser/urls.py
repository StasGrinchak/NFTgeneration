from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register_request, name='register'),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
]