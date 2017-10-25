from django.conf.urls import url

from nutrients_info import views

app_name = 'nutrients_info'

urlpatterns = [
    url(r'^$', views.info, name='info')
]
