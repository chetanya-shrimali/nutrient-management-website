from nutrients_info.models import Season, Disease, People, Geographical, Food, \
    Nutrient
from rest_framework import serializers


class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = '__all__'


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'


class PeopleSerializer(serializers.ModelSerializer):
    nutrient = NutrientSerializer(many=True, read_only=True)

    class Meta:
        model = People
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    nutrient = NutrientSerializer(many=True, read_only=True)

    class Meta:
        model = Food
        fields = '__all__'


class GeographicalSerializer(serializers.ModelSerializer):
    food = FoodSerializer(many=True, read_only=True)
    nutrient = NutrientSerializer(many=True, read_only=True)

    class Meta:
        model = Geographical
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    food = FoodSerializer(many=True, read_only=True)
    nutrient = NutrientSerializer(many=True, read_only=True)

    class Meta:
        model = Season
        fields = '__all__'
