from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView

from user.serializers import UserSerializer, UserProfileSerializer, LoginSerializer
from user.models import User


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class FollowView(APIView):
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        me = request.user
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("언팔로우했습니다.", status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response("팔로우했습니다.", status=status.HTTP_200_OK)


class ProfileView(APIView):

    def get(self, request, user_id):
        profile = get_object_or_404(User, id=user_id)
        if request.user.username == profile.username:
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, user_id):
        profile = get_object_or_404(User, id=user_id)
        if request.user == profile:
            serializer = UserSerializer(
                profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
