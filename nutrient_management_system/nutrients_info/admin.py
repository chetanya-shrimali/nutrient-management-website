from django.contrib import admin

from .models import Food, Nutrient, Disease, Geographical, People, Season, \
    FoodFoundGeographical, FoodFoundSeason, NutrientFoundFood, \
    NutrientGivenPeople

admin.site.register(Food)
admin.site.register(Nutrient)
admin.site.register(Disease)
admin.site.register(Geographical)
admin.site.register(People)
admin.site.register(Season)
admin.site.register(FoodFoundSeason)
admin.site.register(FoodFoundGeographical)
admin.site.register(NutrientFoundFood)
admin.site.register(NutrientGivenPeople)