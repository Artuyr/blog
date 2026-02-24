from django.db import models

#Modelo Author
class Autor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

#Modelo Category    
class Categoria(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

#Modelo Tag
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

#Modelo Post    
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    #Relacionamento Autor-Post (1:N)
    author = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='posts')
    #Relacionamento Categoria-Post (1:N)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='posts')
    #Relacionamento Tag-Post (N:N)
    tags = models.ManyToManyField(Tag, related_name='posts')
    
    def __str__(self):
        return self.title

#Modelo Comment    
class Comentario(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    
    #Relacionamento Post-Comentário (1:N)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comentário de {self.name}'
