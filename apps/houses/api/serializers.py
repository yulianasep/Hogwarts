from rest_framework import serializers

from apps.houses.models import House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"

    def create(self, validated_data):
        name_body = validated_data.get("name")
        new_house= House.objects.create(
            name=name_body
        )
        return new_house
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    