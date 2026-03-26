from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ('publish_article', 'Puede publicar artículos'),
            ('feature_article', 'Puede destacar artículos'),
        ]

    def __str__(self):
        return self.title