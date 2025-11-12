from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from courses.serializer import CourseSerializer, UserSerializer
from .models import Course, User 



@api_view(['GET'])
def course_list_above_20(request):
    courses = Course.objects.filter(duration__gt=20)
    serializer = CourseSerializer(courses, many=True)
    return Response(courses.values(), status=200)

# @api_view(['GET', 'POST'])
# def course_list(request):
#     courses = Course.objects.all()
#     serializer = CourseSerializer(courses, many=True)
#     return Response(serializer.data, status=200)


# @api_view(['GET'])
# class CourseListView(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

@api_view(['GET', 'POST'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def create_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

