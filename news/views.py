from rest_framework import permissions
from .serializers import NewsSerializer, NewsDetailSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView
from .models import News


class NewsDetailView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'


class NewsList(ListAPIView):
    queryset = News.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = NewsSerializer