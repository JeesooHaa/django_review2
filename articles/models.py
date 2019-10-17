from django.db import models
from django.core.validators import EmailValidator, MinValueValidator


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 역순 정렬 / migrate 안해도됨 
    class Meta:
        ordering = ('-pk', )


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pk', )


class Person(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(
        max_length=100, 
        validators=[EmailValidator(message='이메일 형식에 맞지 않습니다.')]
    )
    age = models.IntegerField(
        validators=[MinValueValidator(19, message='미성년자는 노노')]
    )
