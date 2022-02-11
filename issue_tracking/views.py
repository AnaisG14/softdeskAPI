from issue_tracking.models import Project, Issue, Comment, Contributors
from issue_tracking.serializers import (ProjectSerializer,
                                        IssueListSerializer,
                                        CommentSerializer,
                                        UserSerializer,
                                        SignupSerializer,
                                        ContributorSerializer)
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework import permissions
from issue_tracking.permissions import IsOwnerOrReadOnly


class ProjectViewSet(ModelViewSet):
    """ Use CRUD on all projects. """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #     else:
    #         permission_classes = [IsOwnerOrReadOnly]
    #     return [permission() for permission in permission_classes]

    # def perform_create(self, serializer):
    #     serializer.save(author_user_id=self.request.user)


class IssueViewSet(ModelViewSet):
    """ Use CRUD on all issues. """
    serializer_class = IssueListSerializer

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs['project_id_pk'])

    # def perform_create(self, serializer):
    #     serializer.save(author_user_id=self.request.user)

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #     else:
    #         permission_classes = [IsOwnerOrReadOnly]
    #     return [permission() for permission in permission_classes]


class CommentViewSet(ModelViewSet):
    """ List all comments or create a new comment."""

    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs['issue_id_pk'])

    # def get_queryset(self):
    #     queryset = Comment.objects.all()
    #     issue_id = self.request.GET.get('issue_id')
    #     if issue_id is not None:
    #         queryset = queryset.filter(issue_id=issue_id)
    #     return queryset

    # def perform_create(self, serializer):
    #     serializer.save(author_user_id=self.request.user)


class SignupViewSet(ModelViewSet):
    """ Inscription of a user"""

    queryset = User.objects.all()
    serializer_class = SignupSerializer


class UserViewSet(ModelViewSet):
    """ List all users or create a new user."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContributorsViewSet(ModelViewSet):
    """ List all contributors or add a contributor to a project"""

    serializer_class = ContributorSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Contributors.objects.filter(project=self.kwargs['project_id_pk'])


    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #     else:
    #         permission_classes = [IsOwnerOrReadOnly]
    #     return [permission() for permission in permission_classes]
