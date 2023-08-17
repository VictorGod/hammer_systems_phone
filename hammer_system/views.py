from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from time import sleep
import random
from .models import User
from .serializers import UserSerializer

class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['POST'],url_path="authorize")
    def authorize(self, request):
        phone_number = request.data.get('phone_number')
        authorization_code = request.data.get('authorization_code')

        # Имитация задержки на сервере
        sleep(2)

        # Проверка кода авторизации
        user = User.objects.filter(phone_number=phone_number, authorization_code=authorization_code).first()
        if user:
            return Response({'message': 'Авторизация успешна'})
        else:
            return Response({'message': 'Неверный код авторизации'})

    @action(detail=False, methods=['POST'],url_path="profile")
    def profile(self, request):
        phone_number = request.data.get('phone_number')
        invite_code = request.data.get('invite_code')

        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            # Создание нового пользователя
            user = User(phone_number=phone_number)
            user.authorization_code = ''.join(random.choices('0123456789', k=4))
            user.invite_code = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=6))
            user.save()

        if invite_code:
            # Проверка инвайт-кода
            invited_user = User.objects.filter(invite_code=invite_code).first()
            if invited_user:
                user.activated_invite_code = invite_code
                user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'],url_path="invited_users")
    def invited_users(self, request):
        phone_number = request.GET.get('phone_number')

        user = User.objects.filter(phone_number=phone_number).first()
        if user:
            invited_users = User.objects.filter(activated_invite_code=user.invite_code).values_list('phone_number', flat=True)
            return Response({'invited_users': list(invited_users)})
        else:
            return Response({'message': 'Пользователь не найден'})
