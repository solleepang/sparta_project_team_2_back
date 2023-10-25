from rest_framework import serializers

from article.models import Article
from user.models import User


class ArticleSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_member_count(self, obj):
        """ 해당 게시글에 등록된 밥친구 몇명인지 반환 """
        member_count = len(User.objects.filter(user_friend=obj.id))
        return member_count

    def get_username(self, obj):
        """ 작성자의 유저이름 반환 """
        user = User.objects.get(id=obj.author_id.id)
        return user.username
