from rest_framework import viewsets
from .models import Link
from .serializers import LinkSerializer, LinkUrlSerializer
from .utils import get_link_data_from_url
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .permissions import IsOwner
from .filters import OwnerFilter


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsOwner]
    filter_backends = [OwnerFilter]

    # Create your views here.
    @swagger_auto_schema(
        request_body=LinkUrlSerializer, responses={201: LinkSerializer}
    )
    def create(self, request, *args, **kwargs):
        url_serializer = LinkUrlSerializer(
            data=request.data, context={"request": request}
        )
        url_serializer.is_valid(raise_exception=True)
        data = get_link_data_from_url(url_serializer.validated_data["url"])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
