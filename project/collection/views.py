from rest_framework import viewsets, permissions
from .models import Collection
from .serializers import CollectionSerializer, LinkIdSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from link.models import Link
from .permissions import IsOwner
from .filters import OwnerFilter
from drf_yasg.utils import swagger_auto_schema


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [OwnerFilter]

    @swagger_auto_schema(request_body=LinkIdSerializer)
    @action(detail=True, methods=["post"])
    def add_link(self, request, pk=None):
        collection = self.get_object()
        link_id = request.data.get("link_id")
        if not link_id:
            return Response({"error": "Link ID is required."}, status=400)

        try:
            link = Link.objects.get(pk=link_id, user=request.user)
        except Link.DoesNotExist:
            return Response({"error": "Link not found."}, status=404)

        collection.links.add(link)
        return Response({"message": "Link added to collection."}, status=200)

    @swagger_auto_schema(request_body=LinkIdSerializer)
    @action(detail=True, methods=["post"])
    def remove_link(self, request, pk=None):
        collection = self.get_object()
        link_id = request.data.get("link_id")
        if not link_id:
            return Response({"error": "Link ID is required."}, status=400)

        try:
            link = collection.links.get(pk=link_id)
        except Link.DoesNotExist:
            return Response({"error": "Link not found in this collection."}, status=404)

        collection.links.remove(link)
        return Response({"message": "Link removed from collection."}, status=200)
