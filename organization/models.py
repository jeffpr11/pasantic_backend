from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from utils.models import *

# Create your models here.
class Enterprise(BaseModel):
    name = models.CharField(max_length=20)
    description =  models.CharField(max_length=60, blank=True)
    web_site = models.CharField(max_length=50)
    industry = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    contact = models.ForeignKey("user.Agent", on_delete=models.DO_NOTHING, related_name='agent_of_%(class)s')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Enterprises"

class Review(BaseModel):
    description = models.CharField(max_length=50)
    rating = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    owner_enterprise = models.ForeignKey(Enterprise, on_delete=models.DO_NOTHING, related_name='enterprise_of_%(class)s')
    reviewer = models.ForeignKey("user.Intern", on_delete=models.DO_NOTHING, related_name='reviewer_of_%(class)s')

    def __str__(self):
        return f"{self.owner_enterprise.name} {self.rating}"
