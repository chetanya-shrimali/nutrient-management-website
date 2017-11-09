from articles import views
from django.conf.urls import url

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^(?P<pk>[0-9]+)/article/$', views.full_article, name='full_article'),
    url(r'^add/$', views.ArticleFormView.as_view(), name='add_article'),
    url(r'^(?P<pk>[0-9]+)/edit/', views.ArticleUpdate.as_view(),
        name='edit_article'),
    url(r'^(?P<pk>[0-9]+)/delete/', views.ArticleDelete.as_view(),
        name='delete_article')
]
