# tickets/permissions.py

from rest_framework import permissions

class IsOwnerOrAdminOrAgent(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admins/agents to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any authenticated user,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the ticket
        # or to an admin/agent.
        return obj.created_by == request.user or request.user.role in ['admin', 'agent']

class IsAdminOrAgent(permissions.BasePermission):
    """
    Custom permission to only allow admins or agents to access a view.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.is_staff or request.user.role == 'agent'
