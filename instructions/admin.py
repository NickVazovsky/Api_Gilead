from django.contrib import admin
from .models import Instructions

class InstructionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview', 'pdf', 'available', 'created_at', 'updated_at')
    list_display_links = ('id', 'title',)
    list_editable = ('available',)
    search_fields = ('id', 'title',)


admin.site.register(Instructions, InstructionsAdmin)