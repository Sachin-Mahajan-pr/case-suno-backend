from django.db import models

# Create your models here.

from django.db import models


class Professional(models.Model):
    name = models.CharField(max_length=120)

    specialism = models.CharField(max_length=150)

    contact = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.specialism}"
