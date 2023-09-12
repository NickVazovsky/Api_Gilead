from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('name_of_news', 'slug', 'picture_of_news', 'short_description', 'description', 'available_news', 'created_at')


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('name_of_news', 'slug', 'picture_of_news',  'description', 'available_news', 'created_at')
        lookup_field = 'slug'
