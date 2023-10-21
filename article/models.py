from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # friends_ids = models.ManyToManyField('user.User', related_name='user_friend', blank=True) // 유저앱 추가 후 수정
    # author_id = models.ForeignKey(User, on_delete=models.CASCADE) // 유저앱 추가 후 수정
    # store_id = models.ForeignKey(Store, on_delete=models.CASCADE) // 가게 위치 앱 추가 후 수정

    def __str__(self):
        return str(self.title)
