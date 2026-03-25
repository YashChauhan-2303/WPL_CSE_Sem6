from django.db import models


class Category(models.Model):
    """Model for website categories"""
    name = models.CharField(max_length=200, unique=True)
    visits = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['-likes', '-visits']

    def __str__(self):
        return self.name


class Page(models.Model):
    """Model for website pages/links"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pages')
    title = models.CharField(max_length=200)
    url = models.URLField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-views', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.category.name})"
