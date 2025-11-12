from rest_framework import serializers
from .models import AdditionalResource, Category, Course, Teacher, User

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'      


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'      

class  AdditionalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalResource
        fields = '__all__'      


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'              



        