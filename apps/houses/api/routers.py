from rest_framework.routers import DefaultRouter
from apps.houses.views import HouseViewSet

router = DefaultRouter()

router.register(r'houses', HouseViewSet, basename='houses')

urlpatterns = router.urls