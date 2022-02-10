from rest_framework import serializers
from django.contrib.auth.models import User
from issue_tracking.models import Project, Issue, Comment, Contributors


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributors
        fields = ['id', 'user', 'project', 'permission', 'role']


class CommentSerializer(serializers.ModelSerializer):
    author_user_id = serializers.ReadOnlyField(source='author_user_id.username')

    class Meta:
        model = Comment
        fields = ['id', 'description', 'created_date_time', 'issue_id', 'author_user_id']


class IssueListSerializer(serializers.ModelSerializer):
    author_user_id = serializers.ReadOnlyField(source='author_user_id.username')

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'created_date_time', 'project_id', 'author_user_id']


class IssueDetailSerializer(serializers.ModelSerializer):
    comments_issue = CommentSerializer(many=True)
    author_user_id = serializers.ReadOnlyField(source='author_user_id.username')

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'created_date_time', 'project_id', 'author_user_id', 'comments_issue']


class ProjectSerializer(serializers.ModelSerializer):
    contributors = UserSerializer(many=True, read_only=True)
    author_user_id = serializers.ReadOnlyField(source='author_user_id.username')

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user_id', 'contributors']

