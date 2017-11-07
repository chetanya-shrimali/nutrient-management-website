from django.shortcuts import render
from .models import Disease, Food, Geographical, Nutrient, People, Seasonal


def info(request):
    nutrients = Nutrient.objects.all()
    return render(request, 'nutrients_info.html', {'nutrients': nutrients})
