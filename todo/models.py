from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, default=None
    )
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
