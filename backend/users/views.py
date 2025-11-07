from rest_framework import generics, permissions
from .serializers import RegisterSerializer, UserSerializer, MechanicProfileSerializer
from .models import CustomUser, MechanicProfile
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user

class MechanicProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = MechanicProfile.objects.all()
    serializer_class = MechanicProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return MechanicProfile.objects.get(user=self.request.user)
