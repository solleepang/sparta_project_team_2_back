from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = User
        fields = "__all__"
