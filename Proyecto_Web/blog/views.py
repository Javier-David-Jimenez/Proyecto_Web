from django.shortcuts import render
from  blog.models import Post, Categoria

# Create your views here.

def blog(request):
    
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def categoria(request, categoria_id):
    
    categoria = Categoria.objects.get(id = categoria_id)
    posts = Post.objects.filter(categorias = categoria)
    return render(request, "blog/categoria.html", {'categoria': categoria, "posts": posts} )

"""  Metodo para eliminar repeticiones de las categorias en el pie de blog
def mi_vista(request):
    # Obtén todas las publicaciones
    posts = Post.objects.all()

    # Inicializa una lista para almacenar categorías únicas
    categorias_unicas = []

    # Recorre las publicaciones y sus categorías
    for post in posts:
        for categoria in post.categorias.all():
            if categoria not in categorias_unicas:
                categorias_unicas.append(categoria)

    return render(request, 'blog/blog.html', {'posts': posts, 'categorias_unicas': categorias_unicas})"""