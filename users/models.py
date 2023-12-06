from django.db import models
from django.contrib.auth.models import AbstractUser

from locations.models import Country, City

# Create your models here.

class User(AbstractUser):
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, verbose_name='страна')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, verbose_name='город')