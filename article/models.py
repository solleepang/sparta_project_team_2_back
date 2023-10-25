from django.db import models
from user.models import User


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
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    friends_number = models.IntegerField(default=2)
    friends_ids = models.ManyToManyField('user.User', related_name='user_friend', blank=True) 

    def __str__(self):
        return str(self.title)
