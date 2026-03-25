from django.contrib import admin
from .models import Works, Lives


@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    list_display = ['person_name', 'company_name', 'salary', 'created_at']
    search_fields = ['person_name', 'company_name']
    list_filter = ['company_name', 'created_at']
    ordering = ['-created_at']


@admin.register(Lives)
class LivesAdmin(admin.ModelAdmin):
    list_display = ['get_person_name', 'get_company', 'city', 'street', 'created_at']
    search_fields = ['works__person_name', 'city']
    list_filter = ['city', 'created_at']
    ordering = ['-created_at']
    
    def get_person_name(self, obj):
        return obj.works.person_name
    get_person_name.short_description = 'Person Name'
    
    def get_company(self, obj):
        return obj.works.company_name
    get_company.short_description = 'Company'
