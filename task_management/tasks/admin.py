from django.contrib import admin
from .models import Task
# Register your models here.

# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','status', 'created_at', 'updated_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'
    row_id_fields = 'id'
    ordering = ['created_at']
    show_facets = admin.ShowFacets.ALWAYS