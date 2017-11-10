from django.apps import apps
from django.shortcuts import render
from django.views import View
from home.forms import UserForm


def home(request):
    article_model = apps.get_model('articles.Article')
    print(article_model)
    articles = article_model.objects.all().order_by('-id')[:3]
    print(articles)
    return render(request, 'index.html', {'articles': articles})


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {form: form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
