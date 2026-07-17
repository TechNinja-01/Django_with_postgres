from django.urls import path
from .views import UserListCreate

urlpatterns = [
    path("Users/",UserListCreate.as_view()),
]

