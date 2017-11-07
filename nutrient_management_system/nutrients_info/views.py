from django.shortcuts import render

from .models import Disease, Food, Nutrient, Seasonal, People, Geographical


def info(request):
    nutrients = Nutrient.objects.all()
    diseases = Disease.objects.all()
    foods = Food.objects.all()
    seasonal = Seasonal.objects.all()
    people = People.objects.all()
    geographical = Geographical.objects.all()
    return render(request, 'nutrients_info.html', {'nutrients': nutrients,
                                                   'diseases': diseases,
                                                   'foods': foods,
                                                   'seasonal': seasonal,
                                                   'people': people,
                                                   'geographical': geographical
                                                   })
