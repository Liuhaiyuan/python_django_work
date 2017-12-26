from django.shortcuts import render, get_object_or_404
from .models import BlogArticles

def blog_app_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog_app/titles.html", {"blogs":blogs})

def blog_app_article(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, 'blog_app/content.html', {'article' : article, 'publish' : pub})