from rest_framework import serializers
from .models import UserAccount


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('email', 'first_name', 'last_name', 'third_name', 'phone_number')


class UsersRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        exclude = ()
        lookup_field = 'id'
