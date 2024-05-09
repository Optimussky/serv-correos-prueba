from rest_framework import viewsets
from login.models import Login
from login.api.serializer import LoginSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer