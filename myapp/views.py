from random import randint

from rest_framework.views import APIView
from rest_framework import status

from rest_framework.response import Response

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
    parser_classes,
    throttle_classes,
    renderer_classes,
)

from rest_framework import (
    authentication,
    permissions,
    parsers,
    throttling,
    renderers,
)
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer


class UserProfileAPIView(APIView):
    """
    Класс для обновления профиля пользователя
    """
    def get(self, request):
        # получаем данные пользователя
        serializer = UserSerializer(instance=request.user)
        return Response(serializer.data)

    def put(self, request):
        # отправляем отредактированные данные
        serializer = UserSerializer(instance=request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
@authentication_classes([authentication.SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
@parser_classes([parsers.JSONParser])
@throttle_classes([throttling.UserRateThrottle])
@renderer_classes([renderers.JSONRenderer])
def get_random_number(request):
    if request.method == 'POST':
        min_num = request.data.get('min')
        max_num = request.data.get('max')
    else:
        min_num = 1
        max_num = 10

    number = randint(min_num, max_num)
    response = {'random_number': number}
    return Response(response)

# class RandomNumberAPIView(APIView):
#
#     def get(self, request, min_num, max_num):
#         number = randint(min_num, max_num)
#         response = {'random_number': number}
#         return Response(response)
#
#     def post(self, request):
#         min_num = request.data.get('min')
#         max_num = request.data.get('max')
#         number = randint(min_num, max_num)
#         response = {'random_number': number}
#         return Response(response)
#
