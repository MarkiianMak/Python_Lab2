from courses.serializer import  UserSerializer
from ..models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.db.models import Sum
from ..models import Course
from courses.serializer import  CourseSerializer
from django.http import JsonResponse

@api_view(['GET'])
def user_name(request):
    courses = Course.objects.aggregate(total_duration=Sum('duration'))
    return JsonResponse(courses, status=200, safe=False)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
