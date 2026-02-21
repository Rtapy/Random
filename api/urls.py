from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthView, ProjectViewSet, TaskViewSet, CommentViewSet, TaskNPlusOneViewSet


router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"tasks", TaskViewSet, basename="task")
router.register(r"comments", CommentViewSet, basename="comment")
router.register(r"projectList", TaskNPlusOneViewSet, basename="projectList")

urlpatterns = [
    path("health/", HealthView.as_view(), name="health"),
    path("", include(router.urls)),
]