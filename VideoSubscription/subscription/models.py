from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.contrib.auth import get_user_model
# User = get_user_model()
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError("Enter your email.")
        if not username:
            raise ValueError("Enter your username.")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self, email, username, password = None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_active = True
        user.is_admin  = True
        user.is_staff  = True
        user.is_superuser = True

        user.save(using = self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=70, unique=True)
    first_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    email = models.EmailField(max_length=70, unique=True)
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    FREE = 'free'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'
    SUBSCRIPTION = (
        (FREE, 'Free'),
        (MONTHLY, 'Monthly'),
        (YEARLY, 'yearly')
    )
    subscribe = models.CharField(null=True, blank=True, choices=SUBSCRIPTION, max_length=7, default=FREE)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username


class Video(models.Model):
    FREE = 'free'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'
    SUBSCRIPTION = (
        (FREE, 'Free'),
        (MONTHLY, 'Monthly'),
        (YEARLY, 'yearly')
    )
    name = models.CharField(max_length=50)
    discription = models.TextField()
    subscription_type = models.CharField(null=True, blank=True, choices=SUBSCRIPTION, max_length=7, default=FREE)
    image = models.ImageField(upload_to='images/', default='images/thumbnail.jpg')
    video= models.FileField(upload_to='videos/', null=True)


class Subscription(models.Model):
    FREE = "free"
    MONTHLY = "monthly"
    YEARLY = "yearly"
    MEMBERSHIP = (
        (FREE, "free"),
        (MONTHLY, "monthly"),
        (YEARLY, "yearly")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership_type = models.CharField(default=FREE, choices=MEMBERSHIP, max_length=10)
    expiry_date = models.DateTimeField(null=True, blank=True)