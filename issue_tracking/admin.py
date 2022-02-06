from django.contrib import admin
from issue_tracking.models import Project, Issue,Comment

admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
