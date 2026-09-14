from django.contrib import admin
from .models import ContactMessage,Service,Destination
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "travel_dates", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "message")
    ordering = ("-created_at",)
    readonly_fields = ("name", "email", "travel_dates", "message", "created_at")
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "is_active", "image")
    list_display_links = ("title",)
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("order",)

 
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("order", "name", "region", "is_active", "image")
    list_display_links = ("name",)
    list_editable = ("order", "is_active")
    list_filter = ("is_active", "region")
    search_fields = ("name", "region", "short_description", "description")
    ordering = ("order",)
    prepopulated_fields = {"slug": ("name",)}
 