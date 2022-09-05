from django.views.generic import ListView
from articles.models import Article

class ArticleListView(ListView):
    template_name = 'article_list.html'
    model = Article