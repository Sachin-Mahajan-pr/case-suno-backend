from django.contrib import admin
from .models import Requirement


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = (
        "reference_id",
        "name",
        "mobile",
        "city",
        "urgency",
        "status",
        "created_at",
    )
    search_fields = ("reference_id", "name", "mobile", "email")
    list_filter = ("status", "urgency", "city")
    readonly_fields = ("created_at",)
