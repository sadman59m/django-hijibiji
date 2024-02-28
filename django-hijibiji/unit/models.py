from django.db import models

# Create your models here.
# Standard library imports

# Django imports
from django.contrib.auth.models import User
from django.db import models

# Django Rest Framework imports

# Third party imports

# Local imports


class Unit(models.Model):
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    admins = models.ManyToManyField(
        User, related_name="unit_admins"
    )
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
