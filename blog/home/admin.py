from django.contrib import admin
from .models import Autor, Post, Categoria, Tag, Comentario

#Registra os Models no DjangoAdmin
admin.site.register(Autor)
admin.site.register(Tag)
admin.site.register(Comentario)
admin.site.register(Post)
admin.site.register(Categoria)

