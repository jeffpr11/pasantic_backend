from django.db import models


class BaseModel(models.Model):
    date_created = models.DateField(auto_now=True, null=True)
    date_modified = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
