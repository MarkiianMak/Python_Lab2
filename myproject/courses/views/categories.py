from courses.serializer import  CategorySerializer, UserSerializer
from ..models import Category
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
