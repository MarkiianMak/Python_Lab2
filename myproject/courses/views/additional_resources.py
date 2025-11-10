from courses.serializer import  AdditionalResourceSerializer, UserSerializer
from ..models import AdditionalResource
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
class AdditionalResourceViewSet(viewsets.ModelViewSet):
    queryset = AdditionalResource.objects.all()
    serializer_class = AdditionalResourceSerializer
    permission_classes = [IsAuthenticated]  
