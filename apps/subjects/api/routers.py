from rest_framework.routers import DefaultRouter
from apps.subjects.views import SpellViewSet, SubjectViewSet

router = DefaultRouter()

router.register(r'spells', SpellViewSet, basename='spells')
router.register(r'subjects', SubjectViewSet, basename='subjects')

urlpatterns = router.urls
