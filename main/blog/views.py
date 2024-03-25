from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'first_page.html', context)


def aboutme_page(request):
    context = {
    }
    return render(request, 'aboutme.html', context)
