from django.contrib import admin
from django.urls import path, include
from django import views
from main.views import basket_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]



