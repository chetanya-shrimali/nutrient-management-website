from django.db import models


class Article(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    content = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    publisher = models.CharField(max_length=50)
    date = models.DateField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)