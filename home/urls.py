from django.urls import path
from . import views

urlpatterns = [
    #Redireciona para View Pública Home
    path('', views.listapost, name='listapost'),
    #Redireciona para View Pública Detalhamento do Post
    path('post/<slug:slug>/', views.detalhe, name='detalhe'),
    #Redireciona para View Pública Filtro por Categoria
    path('category/<slug:slug>/', views.categoria_post, name='categoria_post'),
    #Redireciona para View Pública Filtro por Autor
    path('author/<int:author_id>/', views.autor_post, name='autor_post'),
    #Redireciona para View Pública Filtro por Tag
    path('tag/<slug:slug>/', views.tag_post, name='tag_post'),
]