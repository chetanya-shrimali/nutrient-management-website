from django.db import models


class Nutrient(models.Model):
    name = models.CharField(max_length=100)
    avg_intake = models.CharField(max_length=1000)


class Disease(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lack = models.BooleanField(default=False)
    surplus = models.BooleanField(default=False)


class People(models.Model):
    people_types = (('athelete', 'athelete'), ('normal', 'normal'), ('pregnant-lady', 'pregnant-lady'))

    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=people_types, default='athelete')


class Food(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Geographical(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Seasonal(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
