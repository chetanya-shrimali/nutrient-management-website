from django.db import models


class Nutrient(models.Model):
    name = models.CharField(max_length=100)
    avg_intake = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Disease(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lack = models.BooleanField(default=False)
    surplus = models.BooleanField(default=False)

    def __str__(self):
        return self.nutrient.name + ' -> ' + self.name


class People(models.Model):
    # people_types = (('athelete', 'athelete'), ('normal', 'normal'),
    #                 ('pregnant-lady', 'pregnant-lady'))

    # nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    # type = models.CharField(max_length=20, choices=people_types,
    #                         default='athelete')
    type = models.CharField(max_length=50, default='type here')

    def __str__(self):
        return self.type


class Food(models.Model):
    # nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Geographical(models.Model):
    # food = models.ForeignKey(Food, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Season(models.Model):
    # food = models.ForeignKey(Food, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FoodFoundInSeason(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return self.food.name + ' -> ' + self.season.name


class FoodFoundInGeographical(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    geographical = models.ForeignKey(Geographical, on_delete=models.CASCADE)

    def __str__(self):
        return self.food.name + ' -> ' + self.geographical.name


class NutrientFoundInFood(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return self.nutrient.name + ' -> ' + self.food.name


class NutrientGivenToPeople(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    people = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.nutrient.name + ' -> ' + self.people.type
