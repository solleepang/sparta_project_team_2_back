from rest_framework import serializers
from user.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):  # HyperlinkedModelSerializer
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        print(user.is_active)
        user.is_active = True
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
        fields = ("image", "username", "nickname",
                  "email", "followings", "followers")


class MyPageSerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    def get_follower_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.followings.count()

    class Meta:
        model = User
        fields = ["username", "nickname",
                  "follower_count", "following_count", "image"]
