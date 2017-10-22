from django.contrib import admin
from .models import Food, Nutrient, Disease, Geographical, People, Seasonal

admin.site.register(Food)
admin.site.register(Nutrient)
admin.site.register(Disease)
admin.site.register(Geographical)
admin.site.register(People)
admin.site.register(Seasonal)
