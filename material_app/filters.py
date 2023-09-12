from .models import Material
from .serializers import MaterialFilterSerializers
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.generics import GenericAPIView


class SliderMaterialFilter(GenericAPIView):
    def get_queryset(self):
        queryset = Material.objects.filter(priority__gt=3).filter(
            roles__name_of_roles=self.request.user.roles.name_of_roles).order_by("?")[:3]
        return queryset


class FilterMaterial(GenericAPIView):
    def get_queryset(self):
        selection_content = self.request.query_params.get('selection', None)
        if selection_content is not None:
            queryset = Material.objects.filter(tags__name_tags=self.tag).filter(
                selection__slug=selection_content).filter(
                roles__name_of_roles=self.request.user.roles.name_of_roles)
            return queryset
        else:
            queryset = Material.objects.filter(tags__name_tags=self.tag).filter(
                roles__name_of_roles=self.request.user.roles.name_of_roles)
            return queryset


class SearchFilterMaterial(ObjectMultipleModelAPIView):
    def get_querylist(self):

        tags = self.request.query_params.get('tags', None)
        products = self.request.query_params.get('product', None)
        content_formats = self.request.query_params.get('content_format', None)
        profile_patients = self.request.query_params.get('profile_patient', None)
        querylist = []

        if tags is not None:
            tag_list = [x for x in tags.replace(' ', '').split(',')]
            querylist.append(
                {
                    'queryset': Material.objects.filter(tags__name_tags__in=tag_list).filter(
                        roles__name_of_roles=self.request.user.roles.name_of_roles),
                    'serializer_class': MaterialFilterSerializers
                },
            )
        if products is not None:
            product_list = [product for product in products.replace(' ', '').split(',')]
            querylist.append(
                {
                    'queryset': Material.objects.filter(product_material__product_name__in=product_list).filter(
                        roles__name_of_roles=self.request.user.roles.name_of_roles),
                    'serializer_class': MaterialFilterSerializers
                },
            )
        if content_formats is not None:
            content_format_list = [content_format for content_format in content_formats.replace(' ', '').split(',')]
            querylist.append(
                {
                    'queryset': Material.objects.filter(content_format__type_name__in=content_format_list).filter(
                        roles__name_of_roles=self.request.user.roles.name_of_roles),
                    'serializer_class': MaterialFilterSerializers
                },
            )
        if profile_patients is not None:
            profiles_list = [profile for profile in profile_patients.replace(' ', '').split(',')]
            querylist.append(
                {
                    'queryset': Material.objects.filter(patient_profile__name_of_profile__in=profiles_list).filter(
                        roles__name_of_roles=self.request.user.roles.name_of_roles),
                    'serializer_class': MaterialFilterSerializers
                },
            )
        return querylist

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
