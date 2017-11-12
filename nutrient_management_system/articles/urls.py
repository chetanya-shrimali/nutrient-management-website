from articles import views
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^(?P<pk>[0-9]+)/article/$', views.full_article, name='full_article'),
    url(r'^add/$', login_required(views.ArticleFormView.as_view()),
        name='add_article'),
    url(r'^(?P<pk>[0-9]+)/edit/',
        login_required(views.ArticleUpdate.as_view()),
        name='edit_article'),
    url(r'^(?P<pk>[0-9]+)/delete/',
        login_required(views.ArticleDelete.as_view()),
        name='delete_article')
]
