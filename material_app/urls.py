from django.urls import path
from .views import (MaterialSearch, DynamicQueryView, HivView, HivDetailView,
SliderView)

urlpatterns = [
    path('sliders/', SliderView.as_view()),
    path('hiv/', HivView.as_view()),
    path('hiv/<slug>', HivDetailView.as_view()),
    path('search/', MaterialSearch.as_view()),
    path('search/filtering/', DynamicQueryView.as_view())
]
