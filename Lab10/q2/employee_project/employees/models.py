from django.db import models


class Works(models.Model):
    """WORKS table: Person employment information"""
    person_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Works"
        ordering = ['company_name', 'person_name']

    def __str__(self):
        return f"{self.person_name} - {self.company_name} (${self.salary})"


class Lives(models.Model):
    """LIVES table: Person location information"""
    works = models.OneToOneField(Works, on_delete=models.CASCADE, related_name='location')
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Lives"
        ordering = ['works__person_name']

    def __str__(self):
        return f"{self.works.person_name} - {self.city}"
    
    @property
    def person_name(self):
        """Get person name from related Works record"""
        return self.works.person_name
