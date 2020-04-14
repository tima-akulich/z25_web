from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return not bool(
            request.method not in SAFE_METHODS and
            request.user and not
            request.user.is_staff
        )
