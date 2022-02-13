from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
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


class CommentSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'issue_pk': 'issue__pk',
        'project_pk': 'issue__project__pk'
    }
    # author_user_id = serializers.ReadOnlyField(source='author_user_id.username')

    class Meta:
        model = Comment
        fields = ['id', 'description', 'created_date_time']


class IssueSerializer(NestedHyperlinkedModelSerializer):

    parent_lookup_kwargs = {
        'project_pk': 'project__pk',
    }
    # author_user_id = serializers.ReadOnlyField(source='author_user_id.username')
    # comments_issue = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'created_date_time', 'projects']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    author_user_id = serializers.ReadOnlyField(source='author_user_id.username')
    contributors = UserSerializer(many=True, read_only=True)
    # issue_project = serializers.HyperlinkedRelatedField(view_name='issue-detail', many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user_id', 'contributors']





