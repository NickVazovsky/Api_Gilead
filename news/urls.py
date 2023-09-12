from django.urls import path
from .views import NewsDetailView, NewsList

urlpatterns = [
    path('', NewsList.as_view()),
    path('<slug>', NewsDetailView.as_view()),
]