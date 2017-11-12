from articles.forms import ArticleForm
from articles.models import Article
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView, DeleteView


def articles(request):
    all_articles = Article.objects.all().order_by('-id')
    return render(request, 'articles.html', {'all_articles': all_articles})


def full_article(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'full_article.html', {'article': article})


class ArticleFormView(View):
    form_class = ArticleForm
    template_name = 'article_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print(self.request.user)
        if form.is_valid():
            post = form.save(commit=False)
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            date = form.cleaned_data['date']
            publisher = form.cleaned_data['publisher']
            post.user = self.request.user
            print(post)
            form.save()
            print(post)

            if post is not None:
                return redirect('articles:articles')
        return render(request, self.template_name, {'form': form})


class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title', 'content', 'publisher', 'date']


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:articles')
