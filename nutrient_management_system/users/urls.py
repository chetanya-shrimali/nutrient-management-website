from django.conf.urls import url

from users import views

app_name = 'users'

urlpatterns = [
    url(r'^$', views.users, name='user'),
    url(r'^register/$', views.UserFormView.as_view(), name='register')
]
