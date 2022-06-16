from rest_framework import serializers

from .models import Adocao
from pet.models import Pet
from pet.serializers import PetSerializer


class AdocaoSerializer(serializers.ModelSerializer):
    pet = PetSerializer(many=False, read_only=True)
    pet_id = serializers.PrimaryKeyRelatedField(
        queryset=Pet.objects.all(), many=False, write_only=True
    )

    class Meta:
        model = Adocao
        fields = ("id", "email", "valor", "pet", "pet_id")

    def create(self, validated_data):
        validated_data["pet"] = validated_data.pop("pet_id")
        return super().create(validated_data)

    def validate_valor(self, value):
        if value < 10:
            raise serializers.ValidationError("Deve ser maior que 10")
        if value > 100:
            raise serializers.ValidationError("Deve ser menor que 100")
        return value