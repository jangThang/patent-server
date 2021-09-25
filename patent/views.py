from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post
# Create your views here.

def descript(request):
    return render(
        request,
        'patent/descript.html'
    )

def word2vec(request):
    return render(
        request,
        'patent/word2vec.html'
    )

def lda(request):
    return render(
        request,
        'patent/LDA.html'
    )

def lsa(request):
    return render(
        request,
        'patent/LSA.html'
    )