from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS \
                and request.user and not request.user.is_staff:
            return False
        return True

