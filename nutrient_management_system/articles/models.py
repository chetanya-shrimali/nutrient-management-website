from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    content = models.TextField()
    publisher = models.CharField(max_length=50)
    date = models.DateField(default='MM/DD/YYYY')

    def __str__(self):
        return self.title + ' -> ' + self.publisher


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.article.title + ' ->' + self.user.username


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.article.title + ' -> ' + self.user.username
