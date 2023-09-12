from django.contrib import admin
from .models import (Material, ProductMaterial, PatientProfiles, Tags,
ContentFormat, SelectionMaterial)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_material', 'slug', 'content_format',
     'created_at', 'updated_at', 'expiration_date')
    list_display_links = ('id', 'name_material',)
    search_fields = ('id', 'name_material',)
    prepopulated_fields = {"slug": ['name_material']}


class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name')
    list_display_links = ('id', 'product_name',)
    search_fields = ('id', 'product_name',)


class PatientProfilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_profile')
    list_display_links = ('id', 'name_of_profile',)
    search_fields = ('id', 'name_of_profile',)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_tags')
    list_display_links = ('id', 'name_tags',)
    search_fields = ('id', 'name_tags',)


class ContentFormatAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    list_display_links = ('id', 'type_name',)
    search_fields = ('id', 'type_name',)


class SelectionMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_selection')
    list_display_links = ('id', 'name_of_selection',)
    search_fields = ('id', 'name_of_selection',)
    prepopulated_fields = {"slug": ['name_of_selection']}


admin.site.register(Material, MaterialAdmin)
admin.site.register(ProductMaterial, ProductMaterialAdmin)
admin.site.register(PatientProfiles, PatientProfilesAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(ContentFormat, ContentFormatAdmin)
admin.site.register(SelectionMaterial, SelectionMaterialAdmin)