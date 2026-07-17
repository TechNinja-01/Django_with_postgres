from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserListCreate
from .views import UserDetail

router = DefaultRouter()
router.register(r'users', UserListCreate, basename='users')

urlpatterns = [
    path("Users/", UserListCreate.as_view(), name="user-list"),
    path("Users/<int:pk>/", UserDetail.as_view(), name="user-detail"),
]