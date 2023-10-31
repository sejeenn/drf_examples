from random import randint

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
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
