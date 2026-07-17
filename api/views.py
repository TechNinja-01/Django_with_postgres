from rest_framework import generics
from .models import Users
from .serializer import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer