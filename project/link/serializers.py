from rest_framework import serializers
from .models import Link
from collection.models import Collection


class LinkUrlSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)

    def validate_url(self, value):

        user = self.context["request"].user
        if Link.objects.filter(user=user, url=value).exists():
            raise serializers.ValidationError("A link with this URL already exists")
        return value


class LinkSerializer(serializers.ModelSerializer):
    collections = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Link
        fields = (
            "id",
            "user",
            "title",
            "description",
            "url",
            "image_url",
            "link_type",
            "created_at",
            "updated_at",
            "collections",
        )
        read_only_fields = ("user", "created_at", "updated_at", "collections")

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user
        return super().create(validated_data)
