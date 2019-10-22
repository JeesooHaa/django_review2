from django.db import models
from django.core.validators import EmailValidator, MinValueValidator
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # models.py 에서만 이렇게 가져옴 
    # article.user
    # user.article_set.all()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 역순 정렬 / migrate 안해도됨 
    class Meta:
        ordering = ('-pk', )


# 1:N 관계가 두개다 
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

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
