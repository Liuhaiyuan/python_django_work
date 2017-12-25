from django.shortcuts import render
from .models import BlogArticles

def blog_app_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog_app/titles.html", {"blogs":blogs})
