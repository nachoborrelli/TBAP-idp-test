from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # add additional fields in here
    pass

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    CHOICES = (
        ('Masculino','Masculino'),
        ('Femenino','Femenino'),
        ('Otro','Otro'),
        ('Prefiero no decirlo','Prefiero no decirlo'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    birthdate = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=30, choices=CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    profile_image = models.ImageField(upload_to = 'profile_image', default = 'profile_image/default.jpg', blank = True, null = True)
    # allow_notifications = models.BooleanField(default=True)
    student_number = models.CharField(max_length=20, null=True, blank=True)
    identification_type = models.CharField(max_length=20, null=True, blank=True)
    identification_number = models.CharField(max_length=20, null=True, blank=True)
    wallet_address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'


class TokenRecovery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=6, default='')
    created_at = models.DateTimeField(auto_now_add=True)