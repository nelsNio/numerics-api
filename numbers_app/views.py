from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from numbers_app.serializer import SerializerInput, NumberSortSerializer
from numbers_app.models import NumberSort


@api_view(['GET'])
def list(request):
    queryset = NumberSort.objects.all()
    serializer = NumberSortSerializer(queryset,many=True)
    return  Response(serializer.data)




@api_view(['POST'])
def render_list(request):
    serializer = SerializerInput(data=request.data)
    if serializer.is_valid(raise_exception=True):
        result = process_data(serializer.data['items'])
        newNumberSorted = NumberSort(numbers={'items':serializer.data['items'],'result': result})
        newNumberSorted.save()
        return Response(data={'result': result}, status=status.HTTP_200_OK)


def process_data(items: list):
    sub_result = []
    for item in items:
        sub_result.append(item) if type(item) == int else sub_result.extend(process_data(item))
    return sub_result
