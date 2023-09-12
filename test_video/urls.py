from django.urls import path
from .views import VideoDetailView, Video

urlpatterns = [
        path('', Video.as_view()),
        path('<slug>', VideoDetailView.as_view())

    ]