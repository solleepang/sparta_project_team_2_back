from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    store_name = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=11, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=11, decimal_places=6, null=True, blank=True)

    # friends_ids = models.ManyToManyField('user.User', related_name='user_friend', blank=True) // 유저앱 추가 후 수정
    # author_id = models.ForeignKey(User, on_delete=models.CASCADE) // 유저앱 추가 후 수정

    def __str__(self):
        return str(self.title)
