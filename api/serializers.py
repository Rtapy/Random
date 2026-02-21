from rest_framework import serializers
from .models import Task, Project, Comment

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description", "created_at", "created_by"]
        read_only_fields = ["id", "created_at", "created_by"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "project", "status", "priority", "created_by", "created_at"]
        read_only_fields = ["id", "created_by", "created_at"]

    def validate_title(self, value: str) -> str:
        if len(value.strip()) < 3:
            raise serializers.ValidationError("This fucking title must be at least 3 fucking characters DumAss...")
        return value
    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "task", "body", "created_at", "created_by"]
        read_only_fields = ["id", "created_at", "created_by"]


class TaskListSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source="project.name", read_only=True)
    created_by_username = serializers.CharField(source="created_by.username", read_only=True)
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Task
        fields = ["id", "title", "status", "priority", "created_at", "created_by", "project", "project_name", "created_by_username", "comment_count"]
        