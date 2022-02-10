"""softdesk_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import routers
from rest_framework_nested import routers
from issue_tracking import views


router = routers.SimpleRouter()
router.register('projects', views.ProjectViewSet, basename='projects')
# router.register('issue', views.IssueViewSet, basename='issue')
# router.register('comment', views.CommentViewSet, basename='comment')
router.register('signup', views.UserViewSet)

projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project_id')
projects_router.register(r'issues', views.IssueViewSet, basename='project-issue')
projects_router.register(r'users', views.ContributorsViewSet, basename='project-user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
]

