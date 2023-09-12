from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Material
from .serializers import (MaterialSerializers, MaterialDetailSerializers,
MaterialFilterSerializers)
from .filters import FilterMaterial, SearchFilterMaterial, SliderMaterialFilter


class SliderView(ListAPIView, SliderMaterialFilter):
    permission_classes = [IsAuthenticated, ]
    serializer_class = MaterialSerializers



class HivView(ListAPIView, FilterMaterial):
    permission_classes = [IsAuthenticated, ]
    serializer_class = MaterialSerializers
    tag = "HIV"


class HivDetailView(RetrieveAPIView, FilterMaterial):
    permission_classes = [IsAuthenticated]
    serializer_class = MaterialDetailSerializers
    tag = "HIV"
    lookup_field = 'slug'


class HbvView(ListAPIView, FilterMaterial):
    permission_classes = [IsAuthenticated, ]
    serializer_class = MaterialSerializers
    tag = "HBV"


class HbvDetailView(RetrieveAPIView, FilterMaterial):
    permission_classes = [IsAuthenticated, ]
    serializer_class = MaterialDetailSerializers
    tag = "HBV"
    lookup_field = 'slug'


class DynamicQueryView(SearchFilterMaterial):
    permission_classes = [IsAuthenticated, ]


class MaterialSearch(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = MaterialFilterSerializers

    def get_queryset(self):
        q = self.request.GET.get('q')
        self.queryset = Material.objects.search(query=q).filter(
            roles__name_of_roles=self.request.user.roles.name_of_roles)
        return self.queryset
        # return self.queryset.filter(roles__name_of_roles=self.request.user.roles.name_of_roles)
