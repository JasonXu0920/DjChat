from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from .schema import server_list_docs
from drf_spectacular.utils import extend_schema

from .models import Server, Category
from .serializer import ServerSerializer, CategorySerializer

# Create your views here.


class CategoryListViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()
    # permission_classes = [IsAuthenticated]

    @server_list_docs
    def list(self, request):
        """
        List servers based on various query parameters.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: A response containing a list of serialized server data.

        Raises:
            AuthenticationFailed: If the user is not authenticated and 'by_user' or 'by_serverid' is specified.
            ValidationError: If server filtering by 'by_serverid' encounters errors, or if a specified server ID is not found.      
        """
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_serverid = request.query_params.get("by_serverid")
        with_num_members = request.query_params.get("with_num_members") == "true"

        # if by_user or by_serverid and not request.user.is_authenticated:
        #    raise AuthenticationFailed()

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        if by_user:
            if by_user and request.user.is_authenticated:
                user_id = request.user.id
                self.queryset = self.queryset.filter(member=user_id)
            else:
                raise AuthenticationFailed()

        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        if qty:
            self.queryset = self.queryset[:int(qty)]    
        
        if by_serverid:
            if not request.user.is_authenticated:
                raise AuthenticationFailed()
            
            try:
                self.queryset = self.queryset.filter(id=by_serverid)
                if not self.queryset.exists():
                    raise ValidationError(detail=f"Server with id {by_serverid} not found")
            except ValueError:
                raise ValidationError(detail="Server value error")
        
        serializer = ServerSerializer(self.queryset, many=True, context={"num_members": with_num_members})
        return Response(serializer.data)
    