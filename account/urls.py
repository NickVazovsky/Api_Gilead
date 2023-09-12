from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView)
from .views import AccountUser, UsersRetrieved

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', AccountUser.as_view(), name='signup'),
    path('users/<id>/', UsersRetrieved.as_view(), name='profile')
]
