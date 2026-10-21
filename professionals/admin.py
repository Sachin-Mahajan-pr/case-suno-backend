
from django.contrib import admin
from .models import Professional


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "specialism", "contact", "is_active")
    search_fields = ("name", "specialism", "contact")
    list_filter = ("specialism", "is_active")
