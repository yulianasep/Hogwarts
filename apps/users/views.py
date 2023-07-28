from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from apps.users.api.serializers import UserSerializer, TeacherSerializer, StudentSerializer
from apps.users.models import CustomUser, Teacher, Student

class UserViewSet(viewsets.ModelViewSet):
    model = CustomUser
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

class TeacherViewSet(viewsets.ModelViewSet):
    model = Teacher
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class StudentViewSet(viewsets.ModelViewSet):
    model = Student
    serializer_class = StudentSerializer
    queryset = Student.objects.all()