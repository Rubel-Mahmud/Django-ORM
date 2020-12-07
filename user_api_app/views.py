from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from user_api_app import serializers



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date__joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]






