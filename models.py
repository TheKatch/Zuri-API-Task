from django.db import models
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank=True, unique=True)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    created_date = models.DateTimeField
    active = models.BooleanField(default=True)


