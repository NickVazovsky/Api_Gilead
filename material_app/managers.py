from django.db import models
from django.db.models import Q


class MaterialManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            # or_lookup = ((Q(name_material__icontains=query) and Q(product_material__product_name=query) and Q(
            #     tags__name_tags=query) and Q(content_format__type_name=query)))
            or_lookup = (Q(name_material__iregex=query) | Q(product_material__product_name__iregex=query) | Q(
                tags__name_tags__iregex=query))
            qs = qs.filter(or_lookup)

        return qs
