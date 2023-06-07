
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext_lazy as _
from users.serializers import UserProfileSerializer, UserSerializer
from oauth2_provider.oauth2_validators import OAuth2Validator
# ProtectedResourceView
from oauth2_provider.views.generic import ProtectedResourceView


class UserProfileMe(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            profile_serializer = UserProfileSerializer(request.user.user_profile)
            user_serializer = UserSerializer(request.user) 
            return Response({'user':user_serializer.data, 'user_profile':profile_serializer.data})
        else:
            return Response({'data': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def patch(self, request):
        if request.user.is_authenticated:
            user_serializer = UserSerializer(data=request.data, instance=request.user, partial=True)
            if user_serializer.is_valid():
                profile_serializer = UserProfileSerializer(data=request.data, instance=request.user.user_profile, partial=True)
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




class TestingOAuth(ProtectedResourceView, APIView):
    """
    A GET endpoint that needs OAuth2 authentication
    """
    def get(self, request, *args, **kwargs):
        return Response('Hello, World!')
