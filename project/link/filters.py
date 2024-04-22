from rest_framework.filters import BaseFilterBackend


class OwnerFilter(BaseFilterBackend):
    """
    Filter objects based on current user as owner.
    """

    def filter_queryset(self, request, queryset, view):

        return queryset.filter(user=request.user)
