from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from articles.models import Article
from django.urls import reverse_lazy

class ArticleListView(ListView):
    template_name = 'article_list.html'
    model = Article

class ArticleCreateView(LoginRequiredMixin, CreateView):
    fields = ['title', 'body']
    template_name = 'article_create.html'
    model = Article
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    model = Article

class ArticleUpdateView(UpdateView):
    template_name = 'article_edit.html'
    model = Article
    fields = ['title', 'body']

class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    model = Article
    success_url = reverse_lazy('article_list')