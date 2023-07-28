from rest_framework.routers import DefaultRouter
from apps.users.views import UserViewSet, TeacherViewSet, StudentViewSet

router = DefaultRouter()

router.register(r'customusers',UserViewSet, basename='customusers')
router.register(r'teachers',TeacherViewSet, basename='teachers')
router.register(r'students',StudentViewSet, basename='students')

urlpatterns = router.urls