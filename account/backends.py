from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password


class UserEmailPhoneBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            if '@' in email:
                user = user_model.objects.get(email__iexact=email)
            else:
                user = user_model.objects.get(phone_number__iexact=email)
            if check_password(password, user.password):
                return user
            else:
                return None
        except user_model.DoesNotExist:
            return None
