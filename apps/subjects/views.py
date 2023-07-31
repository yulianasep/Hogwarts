from rest_framework.response import Response
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404

from apps.subjects.api.serializers import SubjectSerializer, SpellSerializer
from apps.subjects.models import Subject, Spell
from rest_framework.permissions import IsAuthenticated

class SubjectViewSet(viewsets.ModelViewSet):
    model = Subject
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]
    queryset = Subject.objects.all()

class SpellViewSet(viewsets.ModelViewSet):
    model = Spell
    serializer_class = SpellSerializer
    permission_classes = [IsAuthenticated]
    queryset = Spell.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = SpellSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = Spell.objects.all()
        serializer = SpellSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        data = request.data
        instance = get_object_or_404(Spell, pk=pk)
        serializer = SpellSerializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        instance = get_object_or_404(Spell, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, pk=None):
        instance = get_object_or_404(Spell, pk=pk)
        serializer = SpellSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    