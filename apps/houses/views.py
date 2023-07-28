from rest_framework import viewsets


from apps.houses.api.serializers import HouseSerializer
from apps.houses.models import House

class HouseViewSet(viewsets.ModelViewSet):
    model = House
    serializer_class = HouseSerializer
    queryset = House.objects.all()