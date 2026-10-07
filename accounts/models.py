from django.db import models
from django.contrib.auth.models import User

class MostPurchasedUsers(models.Model):
    class Meta:
        app_label = "accounts"
        verbose_name = "Most Purchased Users"
        verbose_name_plural = "Most Purchased Users"

