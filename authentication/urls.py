from django.contrib import admin
from django.urls import path, include
from authenticate_user import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authenticate_user.urls')),
]







