from django.shortcuts import render
from nutrients_info.models import Disease, Food, Nutrient, Season, People, \
    Geographical
from nutrients_info.serializers import SeasonSerializer, FoodSerializer, \
    DiseaseSerializer, GeographicalSerializer, PeopleSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


def info(request):
    nutrients = Nutrient.objects.all()
    diseases = Disease.objects.all()
    foods = Food.objects.all()
    seasons = Season.objects.all()
    peoples = People.objects.all()
    geographicals = Geographical.objects.all()

    return render(request, 'nutrients_info.html', {'nutrients': nutrients,
                                                   'diseases': diseases,
                                                   'foods': foods,
                                                   'seasons': seasons,
                                                   'peoples': peoples,
                                                   'geographicals': geographicals
                                                   })


class SeasonAPI(APIView):
    def get(self, request):
        seasons = Season.objects.all()
        serializer = SeasonSerializer(seasons, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class FoodAPI(APIView):
    def get(self, request):
        food = Food.objects.all()
        serializer = FoodSerializer(food, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class PeopleAPI(APIView):
    def get(self, request):
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class GeographicalAPI(APIView):
    def get(self, request):
        geographical = Geographical.objects.all()
        serializer = GeographicalSerializer(geographical, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class DiseaseAPI(APIView):
    def get(self, request):
        disease = Disease.objects.all()
        serializer = DiseaseSerializer(disease, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

# class NutrientAPI(APIView):
#     def get(self, request):
#         nutrient = Nutrient.objects.all()
#         serializer = DiseaseSerializer(nutrient, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         pass
