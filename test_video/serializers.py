from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('name', 'description', 'slug', 'picture', 'type_media')
        depth = 1


class VideoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        exclude = ()
        lookup_field = 'slug'
        depth = 1