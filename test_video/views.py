from rest_framework.permissions import AllowAny
from .serializers import VideoSerializer, VideoDetailSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView
from .models import Video


class VideoDetailView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializer
    lookup_field = 'slug'


class Video(ListAPIView):
    queryset = Video.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = VideoSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.filter(roles__name_of_roles=self.request.user.roles.name_of_roles)