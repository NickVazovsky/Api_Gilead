from rest_framework import serializers
from .models import Material


class MaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            'name_material', 'slug', 'material_files', 'poster', 'preview',
            'content_format', 'tags', 'selection')
        depth = 1


class MaterialDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            'name_material', 'slug', 'material_files', 'poster', 'preview',
            'content_format', 'product_material',
            'patient_profile', 'tags', 'created_at', 'expiration_date')
        depth = 1


class MaterialFilterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('name_material', 'tags', 'slug', 'selection', 'poster', 'preview', 'content_format')
        depth = 1
