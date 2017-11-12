from django.conf.urls import url

from nutrients_info import views

app_name = 'nutrients_info'

urlpatterns = [
    url(r'^$', views.info, name='info'),
    url(r'^api/season/$', views.SeasonAPI.as_view(), name='season_api'),
    url(r'^api/food/$', views.FoodAPI.as_view(), name='food_api'),
    # url(r'^api/nutrient/$', views.NutrientAPI.as_view(), name='nutrient_api'),
    url(r'^api/people/$', views.PeopleAPI.as_view(), name='people_api'),
    url(r'^api/disease/$', views.DiseaseAPI.as_view(), name='disease_api'),
]
