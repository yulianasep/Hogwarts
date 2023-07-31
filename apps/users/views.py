from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.users.api.serializers import UserSerializer, TeacherSerializer, StudentSerializer
from apps.users.models import CustomUser, Teacher, Student

class UserViewSet(viewsets.ModelViewSet):
    model = CustomUser
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

class TeacherViewSet(viewsets.ModelViewSet):
    model = Teacher
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    queryset = Teacher.objects.all()

class StudentViewSet(viewsets.ModelViewSet):
    model = Student
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()