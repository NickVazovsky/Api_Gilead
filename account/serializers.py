from rest_framework import serializers
from .models import UserAccount


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        exclude = ()
        lookup_field = 'id'
