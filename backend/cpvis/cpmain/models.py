from django.contrib.auth.models import AbstractUser
from django.db import models

class CpUser(AbstractUser):
    leetcode_handle = models.CharField(max_length=100, unique=True, null=True, blank=True)
    codeforces_handle = models.CharField(max_length=100, unique=True, null=True, blank=True)
    codechef_handle = models.CharField(max_length=100, unique=True, null=True, blank=True)
    atcoder_handle = models.CharField(max_length=100, unique=True, null=True, blank=True)
    friends = models.ManyToManyField("self", blank=True)


    def __str__(self):
        return self.username