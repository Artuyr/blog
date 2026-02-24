from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Categoria, Tag, Autor
from .forms import FazerComentario

#View Pública Lista de Posts(Página Inicial)
def listapost(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'home/listapost.html', {'posts': posts})

#View Pública Detalhamento do Post
def detalhe(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comentarios = post.comments.all().order_by('-created_at')

    #Atualiza a lista de comentários quando um novo é feito
    if request.method == 'POST':
        form = FazerComentario(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('detalhe', slug=slug)
    else:
        form = FazerComentario()

    return render(request, 'home/detalhe.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })

#View Pública do Filtro por Categoria
def categoria_post(request, slug):
    category = get_object_or_404(Categoria, slug=slug)
    posts = Post.objects.filter(
        category=category,
        published=True
    ).order_by('-created_at')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'category': category,
        'posts': posts
    }

    return render(request, 'home/categoriapost.html', context)

#View Pública do Filtro por Autor
def autor_post(request, author_id):
    author = get_object_or_404(Autor, id=author_id)
    posts = Post.objects.filter(
        author=author,
        published=True
    ).order_by('-created_at')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'author': author,
        'posts': posts
    }

    return render(request, 'home/autorpost.html', context)

#View Pública do Filtro por Tag
def tag_post(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(
        tags=tag,
        published=True
    ).order_by('-created_at')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'tag': tag,
        'posts': posts
    }

    return render(request, 'home/tagpost.html', context)