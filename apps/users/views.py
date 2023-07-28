from rest_framework import viewsets


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