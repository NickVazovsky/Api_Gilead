from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import UsersSerializer
from rest_framework.decorators import permission_classes

User = get_user_model()


# Create your views here.


class AccountUser(APIView):

    def get(self, request, pk):
        # Получаем набор всех записей из таблицы Capital
        queryset = User.objects.get(pk=pk)
        # Сериализуем извлечённый набор записей
        serializer_for_queryset = UsersSerializer(
            instance=queryset,  # Передаём набор записей
            many=False
        )
        return Response(serializer_for_queryset.data)

    def post(self, request, format=None):
        data = self.request.data
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
        third_name = data['third_name']
        phone_number = data['phone_number']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'Error': 'Email already exists'})
            else:
                if len(password) < 8:
                    return Response({'Error': 'Password  must be at least 8 characters'})
                else:
                    user = User.objects.create_user(email=email, password=password, first_name=first_name,
                                                    last_name=last_name, third_name=third_name,
                                                    phone_number=phone_number)
                    user.save()
                    return Response({'success': 'User sucessfuly'})
        else:
            return Response({'error': 'Password do not match'})
