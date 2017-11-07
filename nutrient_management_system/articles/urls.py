from articles import views
from django.conf.urls import url

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^add/$', views.ArticleFormView.as_view(), name='add_article')
]
