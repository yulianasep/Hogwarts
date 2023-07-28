from rest_framework import serializers

from apps.subjects.models import Spell, Subject
from apps.users.models import Teacher

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
        incantation = validated_data.get("incantation")
        description = validated_data.get("description")

        new_spell= Spell.objects.create(
            name=name_body,
            incantation=incantation,
            description=description
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
            "teacher": "Teacher",
            "credits": "Créditos"
        }

    def create(self, validated_data):
        name_body = validated_data.get("name")
        subject_credits = validated_data.get("credits")
        teacher = Teacher.objects.first()

        new_subject= Subject.objects.create(
            name=name_body,
            teacher=teacher,
            credits=subject_credits
        )
        return new_subject
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['teacher'] = instance.teacher.user.username
        return representation
    