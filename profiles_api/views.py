from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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


class HelloViewSets(viewsets.ViewSet):
    """Test APIViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return Hello message"""
        an_apiview = [
            'Uses actions list, create, retrieve, update, partial_update, destroy',
            'Automatically maps to URL using routers',
            'more funcionalitty with less code'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def create(self, request):
        """Create new Hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}, from viewset"
            return Response({"message": message})
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None):
        """Retrieve and return one resource"""
        return Response({"method": "Retrieve"})

    def update(self, request, pk=None):
        """Retrieve and return one resource"""
        return Response({"method": "update"})

    def partial_update(self, request, pk=None):
        """Retrieve and return one resource"""
        return Response({"method": "partial_update"})

    def destroy(self, request, pk=None):
        """Retrieve and return one resource"""
        return Response({"method": "Destroy"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle management UserProfiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.filter(is_active=True)
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
