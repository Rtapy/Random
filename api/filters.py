import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    project = django_filters.NumberFilter(field_name="project_id")
    status = django_filters.CharFilter(field_name="status")

    class Meta:
        model = Task
        fields = ["project_id", "status"]
        