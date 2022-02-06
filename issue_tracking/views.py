from issue_tracking.models import Project, Issue, Comment
from issue_tracking.serializers import ProjectSerializer, IssueSerializer, CommentSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework import permissions
from issue_tracking.permissions import IsOwnerOrReadOnly


class ProjectList(ListCreateAPIView):
    """ List all projects or create a new project. """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)


class ProjectDetail(RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a project instance."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class IssueList(ListCreateAPIView):
    """ List all projects or create a new issue. """

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)


class IssueDetail(RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete an issue instance."""

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentList(ListCreateAPIView):
    """ List all comments or create a new comment."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)


class CommentDetail(RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a comment instance."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(ListCreateAPIView):
    """ List all users or create a new user."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a user instance."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

