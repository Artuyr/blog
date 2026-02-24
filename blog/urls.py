from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    #Redireciona URLS com "admin/" pro DjangoAdmin
    path('admin/', admin.site.urls),
    #Redireciona todas as outras URLS para urls.py no app home
    path('', include('home.urls')),
]