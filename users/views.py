
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext_lazy as _
from users.serializers import UserProfileSerializer, UserSerializer
from oauth2_provider.oauth2_validators import OAuth2Validator
# ProtectedResourceView
from oauth2_provider.views.generic import ProtectedResourceView


class UserInfo(ProtectedResourceView, APIView):
    def get(self, request):
        user = request.resource_owner
        if user.is_authenticated:
            user_serializer = UserSerializer(user) 
            return Response(user_serializer.data)
        else:
            return Response({'data': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileMe(ProtectedResourceView, APIView):
    def get(self, request):
        user = request.resource_owner
        if user.is_authenticated:
            profile_serializer = UserProfileSerializer(user.user_profile)
            user_serializer = UserSerializer(user) 
            return Response({'user':user_serializer.data, 'user_profile':profile_serializer.data})
        else:
            return Response({'data': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def patch(self, request):
        user = request.resource_owner
        if user.is_authenticated:
            user_serializer = UserSerializer(data=request.data, instance=user, partial=True)
            if user_serializer.is_valid():
                profile_serializer = UserProfileSerializer(data=request.data, instance=user.user_profile, partial=True)
                if profile_serializer.is_valid():
                    user_serializer.save()
                    profile_serializer.save()

                    return Response({'user':user_serializer.data, 'user_profile':profile_serializer.data})
        
                else:
                    return Response(profile_serializer.errors)
            else:
                return Response(user_serializer.errors)
        else:
            return Response({'data': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

