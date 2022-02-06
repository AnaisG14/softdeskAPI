from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """ Stores all information about a project under development.

    Attributes:
        title (str): title project
        description (str): description of the project
        type (str): type of project (front-end, back-end, ios, android)
    """

    TYPE = [('FE', 'front-end'), ('BE', 'back-end'), ('IOS', 'IOS'), ('AND', 'Android')]

    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE)
    author_user_id = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)


class Issue(models.Model):
    """ Stores all information about an issue of a project.

     Attributes:
         title (str): title issue
         description (str): description of the issue
         tag (str): tag of issue (bug, task or improvement)
         priority (str): priority of the issue (low, medium, high)
         status (str): status of the issue (to do, in progress, done)
         created_date_time (date): date of creation of the issue
     """

    TAG = [('bug', 'bug'), ('task', 'task'), ('improvement', 'improvement')]
    PRIORITY = [('low', 'low'), ('medium', 'medium'), ('high', 'high')]
    STATUS = [('to do', 'to do'), ('in progress', 'in progress'), ('done', 'done')]

    title = models.CharField(max_length=100)
    description = models.TextField()
    tag = models.CharField(max_length=50, choices=TAG)
    priority = models.CharField(max_length=50, choices=PRIORITY)
    status = models.CharField(max_length=50, choices=STATUS)
    created_date_time = models.DateTimeField(auto_now_add=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues_project')
    author_user_id = models.ForeignKey(User, related_name='issues', on_delete=models.CASCADE)


class Comment(models.Model):
    """ Stores all information about a comment of a probleme.

     Attributes:
         description (str): description of the issue
         created_date_time (date): date of creation of comment
     """

    description = models.TextField()
    created_date_time = models.DateTimeField(auto_now_add=True)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments_issue')
    author_user_id = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)



# class Contributors(models.Model):
#     """
#         Stores a relation between users and projects.
#     """
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributor')
#     project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projects')
