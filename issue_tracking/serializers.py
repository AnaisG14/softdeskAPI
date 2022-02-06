from rest_framework import serializers
from django.contrib.auth.models import User
from issue_tracking.models import Project, Issue, Comment


class ProjectSerializer(serializers.ModelSerializer):
    issues_project = serializers.PrimaryKeyRelatedField(many=True, queryset=Issue.objects.all())
    author_user_id = serializers.ReadOnlyField(source='author_user_id.username')

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user_id', 'issues_project']


class IssueSerializer(serializers.ModelSerializer):
    comments_issue = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    author_user_id = serializers.ReadOnlyField(source='author_user_id.username')

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'created_date_time', 'project_id', 'author_user_id', 'comments_issue']


class CommentSerializer(serializers.ModelSerializer):
    author_user_id = serializers.ReadOnlyField(source='author_user_id.username')

    class Meta:
        model = Comment
        fields = ['id', 'description', 'created_date_time', 'issue_id', 'author_user_id']


class UserSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    issues = serializers.PrimaryKeyRelatedField(many=True, queryset=Issue.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'projects', 'issues', 'comments']
