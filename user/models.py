from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, nickname, email, password=None):
        if not username:
            raise ValueError("Users must have an username")
        elif not nickname:
            raise ValueError("Users must have an nickname")
        elif not email:
            raise ValueError("Users must have an email")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_superuser(self, username, nickname, email, password=None):
    #     user = self.create_user(
    #         username=username,
    #         password=password,
    #     )
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, username, nickname, email, password=None):
        if password is None:
            raise ValueError("Superuser must have a password")

        user = self.create_user(
            username=username,
            nickname=nickname,
            email=email,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField("아이디", max_length=50, unique=True)
    password = models.CharField("비밀번호", max_length=255)
    email = models.EmailField("이메일 주소", max_length=255)
    nickname = models.CharField("닉네임", max_length=20)
    created_at = models.DateTimeField("가입일", auto_now_add=True)
    updated_at = models.DateTimeField("갱신일", auto_now=True)
    image = models.ImageField(
        default='default_image.jpeg', null=True, blank=True)
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers", blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nickname", "email"]

    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
