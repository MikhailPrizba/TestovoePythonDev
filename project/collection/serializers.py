# serializers.py

from rest_framework import serializers
from .models import Collection
from link.models import Link


class CollectionSerializer(serializers.ModelSerializer):
    links = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = (
            "id",
            "name",
            "description",
            "user",
            "created_at",
            "updated_at",
            "links",
        )
        read_only_fields = ("user", "created_at", "updated_at", "links")

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user
        return super().create(validated_data)


class LinkIdSerializer(serializers.Serializer):
    link_id = serializers.IntegerField(required=True)
