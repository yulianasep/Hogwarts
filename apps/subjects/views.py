from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from apps.subjects.api.serializers import SubjectSerializer, SpellSerializer
from apps.subjects.models import Subject, Spell

class SubjectViewSet(viewsets.ModelViewSet):
    model = Subject
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SpellViewSet(viewsets.ModelViewSet):
    model = Spell
    serializer_class = SpellSerializer
    queryset = Spell.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = SpellSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        data = request.data
        instance = get_object_or_404(Spell, pk=pk)
        serializer = SpellSerializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)