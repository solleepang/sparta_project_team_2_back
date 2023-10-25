from rest_framework import serializers
from user.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        print(user.is_active)
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()  # DB에 전달
        return user


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['username'] = user.username
        token['image'] = user.image.url

        return token


class UserProfileSerializer(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ("image", "username", "nickname", "followings", "followers")
