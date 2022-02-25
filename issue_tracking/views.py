from issue_tracking.models import Project, Issue, Comment, Contributors
from issue_tracking.serializers import (ProjectSerializer,
                                        IssueSerializer,
                                        CommentSerializer,
                                        UserSerializer,
                                        SignupSerializer,
                                        ContributorSerializer)
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import permissions
from issue_tracking.permissions import (IsOwnerOrReadOnly,
                                        CanAdminContributors,
                                        HasContributorPermission)


class ProjectViewSet(ModelViewSet):
    """ Use CRUD on all projects. """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        contributors = [project.contributors.through.objects.all() for project in self.queryset]
        contributors_project = []
        for contributor in contributors:
            for instance in contributor:
                if instance.user == self.request.user:
                    contributors_project.append(instance.project.id)

        return Project.objects.filter(
            id__in=contributors_project) | Project.objects.filter(author_user_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)


class IssueViewSet(ModelViewSet):
    """ Use CRUD on all issues. """

    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, HasContributorPermission]

    def get_queryset(self):
        issues = Issue.objects.filter(projects=self.kwargs['project_pk'])
        return issues

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["projects"] = kwargs["project_pk"]
        request.data["assigned_user_id"] = request.user.pk
        request.POST._mutable = False
        return super(IssueViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["projects"] = kwargs["project_pk"]
        request.POST._mutable = False
        return super(IssueViewSet, self).update(request, *args, **kwargs)


class CommentViewSet(ModelViewSet):
    """ List all comments or create a new comment."""

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, HasContributorPermission]

    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs['issue_pk'])

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["issue_id"] = kwargs["issue_pk"]
        request.data["author_user_id"] = self.request.user.pk
        request.POST._mutable = False
        return super(CommentViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["issue_id"] = kwargs["issue_pk"]
        request.data["author_user_id"] = self.request.user.pk
        request.POST._mutable = False
        return super(CommentViewSet, self).update(request, *args, **kwargs)


class SignupViewSet(ModelViewSet):
    """ Inscription of a user"""

    queryset = User.objects.all()
    serializer_class = SignupSerializer


class UserViewSet(ModelViewSet):
    """ List all users or create a new user."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContributorsViewSet(ModelViewSet):
    """ List all contributors or admin contributors of a project"""

    serializer_class = ContributorSerializer
    permission_classes = [CanAdminContributors, HasContributorPermission]

    def get_queryset(self):
        return Contributors.objects.filter(project=self.kwargs['project_pk'])

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["project"] = kwargs["project_pk"]
        request.POST._mutable = False
        return super(ContributorsViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["project"] = kwargs["project_pk"]
        request.POST._mutable = False
        return super(ContributorsViewSet, self).create(request, *args, **kwargs)
