from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано в:')
    is_complete = models.BooleanField(default=False)

class SignUp(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()