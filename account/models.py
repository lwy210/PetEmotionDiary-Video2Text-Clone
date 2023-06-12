from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        birth_day,
        user_name,
        nick_name,
        update_time,
        password=None,
    ):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            birth_day=birth_day,
            user_name=user_name,
            nick_name=nick_name,
            create_time=timezone.now(),
            update_time=update_time,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            birth_day=timezone.now(),
            nick_name="super",
            user_name="super",
            update_time=timezone.now(),
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=45,
        unique=True,
    )

    user_name = models.CharField(max_length=15)
    nick_name = models.CharField(max_length=15)

    birth_day = models.DateField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
