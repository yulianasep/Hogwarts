from rest_framework import serializers

from apps.houses.models import House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"

    def create(self, validated_data):
        name = validated_data.get("name")
        mascot = validated_data.get("mascot")
        head_of_house = validated_data.get("head_of_house")
        house_ghost = validated_data.get("house_ghost")
        founder = validated_data.get("founder")
        school = validated_data.get("school")

        new_house= House.objects.create(
            name=name,
            mascot=mascot,
            head_of_house=head_of_house,
            house_ghost=house_ghost,
            founder=founder,
            school=school
        )
        return new_house
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    