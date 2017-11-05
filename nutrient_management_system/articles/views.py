from django.shortcuts import render
from .models import Article


def articles(request):
    return render(request, 'articles.html')
