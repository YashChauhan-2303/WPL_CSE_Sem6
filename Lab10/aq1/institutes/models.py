from django.db import models


class Institute(models.Model):
    """Institutes table model"""
    institute_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    no_of_courses = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Institutes"

    def __str__(self):
        return f"{self.name} ({self.no_of_courses} courses)"
