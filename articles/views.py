from django.shortcuts import render
from re import template
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class ArticleListView(ListView):
    template_name = "article_list.html"
    model = Article

class ArticleDetailView(DetailView):
    template_name = "article_detail.html"
    model = Article

class ArticleCreateView( LoginRequiredMixin, CreateView):
    template_name = "article_new.html"
    model = Article
    fields = ["title", "author", "body"]

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "article_edit.html"
    model = Article
    fields = ["title", "author", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "article_delete.html"
    model = Article
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
