from django.db import models
from django.utils.text import slugify


class Person(models.Model):
    name = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if self.name:
            self.username = slugify(self.name)
        return super().save(*args, **kwargs)
