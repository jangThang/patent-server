from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),

    path('descript/', views.descript),
    path('word2vec/', views.word2vec),
    path('lda/', views.lda),
    path('lsa/', views.lsa)
]
