from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from apps.houses.api.serializers import HouseSerializer
from apps.houses.models import House

class HouseViewSet(viewsets.ModelViewSet):
    model = House
    serializer_class = HouseSerializer
    queryset = House.objects.all()