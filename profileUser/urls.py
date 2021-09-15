from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
=======
    path('home/', views.home, name='home'),
    path('register/', views.register_request, name='register'),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("user/", views.userpage, name = "userpage"),
>>>>>>> f1fec3e20fd9590816d787a6fbd14925225108a7
]