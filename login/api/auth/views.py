from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from login.models import Login
from login.api.serializer import LoginSerializer

class LoginViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Login.objects.all()
    serializer_class = LoginSerializer