from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from .models import Book

class OwnerOfTheBookOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions are only allowed to the author of the post.
        return obj.book.author == request.user
