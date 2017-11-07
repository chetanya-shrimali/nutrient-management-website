from django.shortcuts import render

from .models import Disease, Food, Nutrient


def info(request):
    nutrients = Nutrient.objects.all()
    diseases = Disease.objects.all()
    foods = Food.objects.all()
    return render(request, 'nutrients_info.html', {'nutrients': nutrients,
                                                   'diseases': diseases,
                                                   'foods': foods})
