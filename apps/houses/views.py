from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from apps.houses.api.serializers import HouseSerializer
from apps.houses.models import House

class HouseViewSet(viewsets.ModelViewSet):
    model = House
    serializer_class = HouseSerializer
    permission_classes = [IsAuthenticated]
    queryset = House.objects.all()
