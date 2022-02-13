from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """ Stores all information about a project under development.

    Attributes:
        title (str): title project
        description (str): description of the project
        type (str): type of project (front-end, back-end, ios, android)
    """

    TYPE = [('front-end', 'front-end'), ('back-end', 'back-end'), ('IOS', 'IOS'), ('android', 'android')]

    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE)
    author_user_id = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    contributors = models.ManyToManyField(User, through='Contributors', related_name='contributors')

    def __str__(self):
        return f"{self.id}: {self.title}"


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
    projects = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issue_project')
    author_user_id = models.ForeignKey(User, related_name='author_issue', on_delete=models.CASCADE)
    assigned_user_id = models.ForeignKey(User, related_name='assigned', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} : {self.title} : {self.projects}"


class Comment(models.Model):
    """ Stores all information about a comment of a problem.

     Attributes:
         description (str): description of the issue
         created_date_time (date): date of creation of comment
     """

    description = models.TextField()
    created_date_time = models.DateTimeField(auto_now_add=True)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments_issue')
    author_user_id = models.ForeignKey(User, related_name='author_comment', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} in {self.issue_id.title}"


class Contributors(models.Model):
    """ It is a through table storing relation between projects and users."""

    PERMISSIONS = [
        ('read', 'read'),
        ('admin', 'admin'),
    ]

    ROLES = [
        ('author', 'author'),
        ('contributor', 'contributor')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    permission = models.CharField(max_length=10, choices=PERMISSIONS, default='read')
    role = models.CharField(max_length=50, choices=ROLES, default='contributor')

    def __str__(self):
        return f"{self.id}: User: {self.user} -> Project {self.project.title}"
