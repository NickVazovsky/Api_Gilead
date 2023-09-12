from django.contrib import admin
from .models import Video, TypeMedia

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'slug', 'picture', 'type_media')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name')
    prepopulated_fields = {"slug": ['name']}


admin.site.register(Video, VideoAdmin)
admin.site.register(TypeMedia)