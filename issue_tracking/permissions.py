from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.shortcuts import get_object_or_404
from .models import Contributors, Project


class IsOwnerOrReadOnly(BasePermission):
    """ Custom permission to only allow owners of an object to edit it. """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user == obj.author_user_id)


class CanAdminContributors(BasePermission):
    """ Custom permission to only allow the author of the project to add or
    delete contributors in the project. """

    message = "You are not the author of the project."

    def has_permission(self, request, view):
        project_id = request.resolver_match.kwargs['project_pk']
        project = get_object_or_404(Project, pk=project_id)
        if request.method in SAFE_METHODS:
            return True
        elif project.author_user_id == request.user:
            return True
        return False


class HasContributorPermission(BasePermission):
    """ Custom permission to only allow the contributors of the project to
    see issues and comments.
    Only the author of the issue or comment can modify or delete it.
    """

    def has_permission(self, request, view):
        project_id = request.resolver_match.kwargs['project_pk']
        project = get_object_or_404(Project, pk=project_id)
        contributors = Contributors.objects.filter(project=project, user=request.user)
        if project.author_user_id == request.user or len(contributors) != 0:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author_user_id == request.user
