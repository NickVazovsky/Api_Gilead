from django.urls import path
from .views import InstructionView


urlpatterns = [
        path('', InstructionView.as_view())
    ]