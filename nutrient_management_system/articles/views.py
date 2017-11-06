from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import user_logged_in
from articles.forms import ArticleForm
from .models import Article


def articles(request):
    return render(request, 'articles.html')


class ArticleFormView(View):
    form_class = ArticleForm
    template_name = 'registration_form.html'

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
            form.user = self.request.user
            form.save()

            if post is not None:
                return redirect('articles:articles')
        return render(request, self.template_name, {'form': form})
