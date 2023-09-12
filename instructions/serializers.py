from rest_framework import serializers
from .models import Instructions


class InstructionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Instructions
        fields = ('title', 'preview', 'pdf', 'available')
