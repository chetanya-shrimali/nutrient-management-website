from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from nutrients_info import views

app_name = 'nutrients_info'

urlpatterns = [
    url(r'^$', views.info, name='info'),
    url(r'^api/season/$', login_required(views.SeasonAPI.as_view()),
        name='season_api'),
    url(r'^api/food/$', login_required(views.FoodAPI.as_view()),
        name='food_api'),
    # url(r'^api/nutrient/$', views.NutrientAPI.as_view(),
    # name='nutrient_api'),
    url(r'^api/people/$', login_required(views.PeopleAPI.as_view()),
        name='people_api'),
    url(r'^api/disease/$', login_required(views.DiseaseAPI.as_view()),
        name='disease_api'),
]
