from django.contrib import admin

from nutrients_info.models import Food, Nutrient, Disease, Geographical, \
    People, Season, \
    FoodFoundInGeographical, NutrientFoundInFood, NutrientGivenToPeople, \
    FoodFoundInSeason


admin.site.register(Food)
admin.site.register(Nutrient)
admin.site.register(Disease)
admin.site.register(Geographical)
admin.site.register(People)
admin.site.register(Season)
admin.site.register(FoodFoundInGeographical)
admin.site.register(FoodFoundInSeason)
admin.site.register(NutrientGivenToPeople)
admin.site.register(NutrientFoundInFood)

