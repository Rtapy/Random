from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from core.pagination import SetPagination
from rest_framework.pagination import CursorPagination
from .filters import TaskFilter
from django.db import reset_queries, connection


class CursorOrdering(CursorPagination):
    ordering = "-created_at"
    

class HealthView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        # request_id = 75#request.request_id
        return Response({"status": "fucking", "request_id":"request_id"})
    


    


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = SetPagination
    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user).order_by("-id")
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = SetPagination
    filterset_class = TaskFilter
    ordering_fields = ["created_at", "priority"]
    ordering = ["-created_at"]

    

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user).order_by("-id")
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CursorOrdering
    def get_queryset(self):
        return Comment.objects.filter(created_by=self.request.user).order_by("id")
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskNPlusOneViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TaskListSerializer


    def get_queryset(self):
        return Task.objects.all().order_by("-created_at")
    
    
    def list(self, request, *args, **kwargs):
        reset_queries()
        response = super().list(request, *args, **kwargs)
        print("N+1 query count:", len(connection.queries))
        return response
    
