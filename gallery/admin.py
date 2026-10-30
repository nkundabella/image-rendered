from django.contrib import admin
from django.utils.html import format_html
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_preview', 'uploaded_at')
    list_display_links = ('title',)
    search_fields = ('title', 'caption')
    readonly_fields = ('uploaded_at', 'thumbnail_preview')

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 6px;" />',
                obj.image.url
            )
        return "No image"

    thumbnail_preview.short_description = "Preview"
