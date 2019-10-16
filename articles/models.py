from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 역순 정렬 / migrate 안해도됨 
    class Meta:
        ordering = ('-pk', )
        