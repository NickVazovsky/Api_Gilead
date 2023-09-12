from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_news', 'slug', 'picture_of_news', 'description', 'available_news')
    list_display_links = ('id', 'name_of_news',)
    search_fields = ('id', 'name_of_news',)
    prepopulated_fields = {"slug": ['name_of_news'], "short_description":['name_of_news']}


admin.site.register(News, NewsAdmin)