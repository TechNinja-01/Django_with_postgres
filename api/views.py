from rest_framework import generics
from .models import Users
from .serializer import UserSerializer



# Create your views here.
class UserListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

