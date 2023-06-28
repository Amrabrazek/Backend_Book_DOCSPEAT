
from rest_framework.permissions import BasePermission

class IsAccountOwner(BasePermission):
    message = 'You must be the owner of this account to edit or delete it.'

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj == request.user
        return True