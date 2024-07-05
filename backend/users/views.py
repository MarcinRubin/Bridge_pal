from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import (
    ProfileSerializer,
    UserSerializer
)


@method_decorator(ensure_csrf_cookie, name="dispatch")
class GetCSRFToken(APIView):
    """Generate and send the CSRF Token to client"""
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return JsonResponse({"success": "CSRF token set"})


@method_decorator(csrf_protect, name="dispatch")
class UserRegistration(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_protect, name="dispatch")
class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user and user.is_active:
            login(request, user)
            return Response(
                {"detail": "Logged in sucesfully.", "user": username},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"detail": "Incorrect username or password"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class UserLogout(APIView):
    def post(self, request):
        logout(request)
        return Response(
            {"detail": "Logged out successfully."}, status=status.HTTP_200_OK
        )


class ActiveSession(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        if request.user.is_authenticated:
            return Response(
                {
                    "username": request.user.username,
                    "isAuthenticated": True,
                    "active_game": request.user.profile.active_game,
                }
            )
        return Response({"isAuthenticated": False})


