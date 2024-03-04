from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy


# Create your views here : ).

class ArticleListView(ListView):
    model = Article
    template_name = "home.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "post_detail.html"

class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ["title", "author", "body"]

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ['title', 'body']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("home")