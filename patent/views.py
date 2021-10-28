from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import Post

import urllib.request
from urllib.parse import unquote_plus, quote
import json
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
        search = quote(request.POST['word2vecSearch'])
        if search == "":
            return render(request, 'patent/word2vec.html')

        url = 'http://localhost:12354/W2V/'+search
        with urllib.request.urlopen(url) as response:
            result = response.read()
        result = result.decode('utf-8')
        search = unquote_plus(search)

        getJson = json.loads(result)
        retItems = []

        for item in getJson[::-1]:
            keyword = item.pop(0)
            str = 'Terms related to \"' + keyword + "\"=> " + ', '.join(item)
            retItems.append(str)

        return render(request, 'patent/word2vec.html', {'search': search, 'retItems': retItems })

def lda(request):
    # 페이지 불러오기
    if request.method == 'GET':
        return render(request, 'patent/LDA.html')

    # 페이지 내 POST 발생
    elif request.method == 'POST':
        search = quote(request.POST['LDASearch'])
        if search == "":
            return render(request, 'patent/LDA.html')

        url = 'http://localhost:12354/LDA/'+search
        with urllib.request.urlopen(url) as response:
            result = response.read()
        result = result.decode('utf-8')
        search = unquote_plus(search)

        getJson = json.loads(result)
        retItems = []

        for item in getJson:
            item[1] = item[1].replace("+", ",")
            retItems.append(item[1])

        return render(request, 'patent/LDA.html', {'search': search, 'retItems': retItems})

def lsa(request):
    # 페이지 불러오기
    if request.method == 'GET':
        return render(request, 'patent/LSA.html')

    # 페이지 내 POST 발생
    elif request.method == 'POST':
        search = quote(request.POST['LSASearch'])
        if search == "":
            return render(request, 'patent/lsa.html')

        url = 'http://localhost:12354/LSA/'+search
        with urllib.request.urlopen(url) as response:
            result = response.read()
        result = result.decode('utf-8')
        search = unquote_plus(search)

        getJson = json.loads(result)
        retItems = getJson

        return render(request, 'patent/LSA.html', {'search': search, 'retItems': retItems})