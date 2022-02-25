from rest_framework import serializers
from django.contrib.auth.models import User
from issue_tracking.models import Project, Issue, Comment, Contributors


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributors
        fields = ['id', 'user', 'project', 'permission', 'role']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'description', 'created_date_time', 'author_user_id', 'issue_id']


class IssueSerializer(serializers.ModelSerializer):

    author_user_id = serializers.ReadOnlyField(source='author_user_id.username')

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority',
                  'status', 'created_date_time', 'projects', 'author_user_id', 'assigned_user_id']


class ProjectSerializer(serializers.ModelSerializer):
    author_user_id = serializers.ReadOnlyField(source='author_user_id.username')

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user_id']
