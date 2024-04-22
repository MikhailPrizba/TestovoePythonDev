from rest_framework import permissions
from user.models import User


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        # Instance must have an attribute named `owner`.
        return obj.user == request.user
