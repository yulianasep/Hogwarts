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
        name_body = validated_data.get("name")
        new_spell= Spell.objects.create(
            name=name_body
        )
        return new_spell
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['subject'] = instance.subject.name
        return representation

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
        labels = {
            "name": "Nombre",
            "professor": "Profesor",
            "credits": "Créditos"
        }

    def create(self, validated_data):
        name_body = validated_data.get("name")
        new_subject= Subject.objects.create(
            name=name_body
        )
        return new_subject
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['professor'] = instance.professor.user.username
        return representation
    
        