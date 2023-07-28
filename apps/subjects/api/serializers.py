from rest_framework import serializers

from apps.subjects.models import Spell, Subject

class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = "__all__"
        labels = {
            "name": "Nombre",
            "incantation": "Encantamiento",
            "description": "Descripción"
        }

    def create(self, validated_data):
        name_spell = validated_data.get("name")
        new_spell= Spell.objects.create(
            name=name_spell
        )
        return new_spell
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
        labels = {
            "name": "Nombre",
            "professor": "Profesor",
            "credits": "Créditos"
        }
        