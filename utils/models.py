from datetime import date
from django.db import models


class BaseModel(models.Model):
    date_created = models.DateField(default=date.today, auto_now=False, null=True)
    date_modified = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
