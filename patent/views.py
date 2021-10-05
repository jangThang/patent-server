from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import Post

from django.views import View


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
    # 페이지 불러오기
    if request.method == 'GET':
        return render(request, 'patent/word2vec.html')
    # 페이지 내 POST 발생
    elif request.method == 'POST':
        search = request.POST['word2vecSearch']
        return redirect('patent/word2vec/'+search)

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