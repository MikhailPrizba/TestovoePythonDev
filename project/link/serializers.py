from rest_framework import serializers
from .models import Link

class LinkUrlSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'user', 'title', 'description', 'url', 'image_url', 'link_type', 'created_at', 'updated_at')
        read_only_fields = ('user', 'created_at', 'updated_at')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)