from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .models import Pet
from .serializers import PetSerializer


class PetList(APIView):
    def get(self, request, format=None):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, fromat=None):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "message": "Houveram erros de validação",
                "errors": serializer.errors,
            },
            status=HTTP_400_BAD_REQUEST,
        )
        