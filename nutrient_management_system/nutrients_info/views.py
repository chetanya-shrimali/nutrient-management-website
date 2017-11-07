from django.shortcuts import render

from .models import Disease, Food, Nutrient, Seasonal, People, Geographical


def info(request):
    nutrients = Nutrient.objects.all()
    diseases = Disease.objects.all()
    foods = Food.objects.all()
    seasonals = Seasonal.objects.all()
    peoples = People.objects.all()
    geographicals = Geographical.objects.all()
    return render(request, 'nutrients_info.html', {'nutrients': nutrients,
                                                   'diseases': diseases,
                                                   'foods': foods,
                                                   'seasonals': seasonals,
                                                   'peoples': peoples,
                                                   'geographicals': geographicals
                                                   })
