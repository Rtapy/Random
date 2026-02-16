from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class HealthView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        # request_id = 75#request.request_id
        return Response({"status": "fucking", "request_id":"request_id"})
    


    


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user).order_by("-id")
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user).order_by("-id")
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Comment.objects.filter(created_by=self.request.user).order_by("id")
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)