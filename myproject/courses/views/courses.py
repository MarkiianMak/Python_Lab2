from django.http import JsonResponse
from courses.serializer import  CourseSerializer, UserSerializer
from courses.views import users
from ..models import Course, User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.db.models import Sum

@api_view(['GET'])
def course_list_above_20(request):
    courses = Course.objects.aggregate(Number_of_Courses=Sum('courseId'), total_duration=Sum('duration'), average_duration=Sum('duration')/Sum('courseId'))
    return JsonResponse(courses, status=200, safe=False)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]