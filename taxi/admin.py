from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ["manufacturer"]
    search_fields = ["model"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = list(UserAdmin.list_display) + ["license_number"]
    fieldsets = list(UserAdmin.fieldsets) + [("Additional info", {"fields": ("license_number",)})]
    add_fieldsets = list(UserAdmin.add_fieldsets) + [("Additional info", {"fields": ("license_number",)})]


admin.site.register(Manufacturer)
