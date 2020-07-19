from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API VIew"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return list of API features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional DJango View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with name received in post"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}, Welcome to HelloApiView'
            return Response({"message": message})

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        """Handle update object"""
        return Response({"method": 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete the object"""
        return Response({"method": "DELETE"})
