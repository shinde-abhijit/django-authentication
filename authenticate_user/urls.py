from django.urls import path, include
from authenticate_user import views



urlpatterns = [
    path('', views.register_user, name='register-user'),
    path('login/', views.login_user, name='login-user'),
    path('logout/', views.logout_user, name='logout-user'),
    path('homepage/', views.homepage, name='homepage'),
]