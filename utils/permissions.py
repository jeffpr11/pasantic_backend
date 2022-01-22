from rest_framework import permissions


class OnCreateAndUpdateOwnerOnly(permissions.BasePermission):
    """
        Custom permission:
            - allow anonymous POST
            - allow authenticated GET and PUT on *own* record
            - allow all actions for staff
    """

    def has_permission(self, request, view):
        return view.action == 'create' or request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return view.action in ['retrieve', 'update', 'partial_update'] and obj.id == request.user.id or request.user.is_staff


class ListAdminOnly(permissions.BasePermission):
    """
        Custom permission to only allow access to lists for admins
    """

    def has_permission(self, request, view):
        return view.action != 'list' or request.user and request.user.is_staff
