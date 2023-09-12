from rest_framework.generics import ListAPIView
from rest_framework import permissions
from .serializers import InstructionSerializers
from .models import Instructions
# Create your views here.


class InstructionView(ListAPIView):
    queryset = Instructions.objects.filter(available=True)
    serializer_class = InstructionSerializers
    permission_classes = (permissions.IsAuthenticated, )