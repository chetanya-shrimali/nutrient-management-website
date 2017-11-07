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
    people_types = (('athelete', 'athelete'), ('normal', 'normal'),
                    ('pregnant-lady', 'pregnant-lady'))

    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=people_types,
                            default='athelete')

    def __str__(self):
        return self.nutrient.name + ' -> ' + self.type


class Food(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.nutrient.name + ' -> ' + self.name


class Geographical(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Seasonal(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
