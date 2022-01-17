from django.db import models

from django.contrib.postgres.fields import ArrayField
from utils.models import *

class Internship(BaseModel):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=60, blank=True)
    type_of_workDay = models.CharField(max_length=15)
    requirements = ArrayField(models.CharField(max_length=15), size=5, blank=True, null=True)
    challenges = ArrayField(models.CharField(max_length=15), size=5, blank=True, null=True)
    profile = models.CharField(max_length=20)
    start_date = models.DateField(auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False, blank=True, null=True)
    duration_months = models.IntegerField(max_length=2)
    remuneration = models.DecimalField(max_digits= 6, decimal_places=3)
    have_remuneration = models.BooleanField(default=False)
    owner_enterprise = models.ForeignKey("organization.Enterprise", on_delete=models.DO_NOTHING, related_name='enterprise_of_%(class)s')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Internships"


class Postulation(BaseModel):
    post_date = models.DateField(auto_now=True, null=True)
    state = models.BooleanField(default=True)
    postulant = models.ForeignKey("user.Intern", on_delete=models.DO_NOTHING, related_name='profile_of_%(class)s')
    internship = models.ForeignKey(Internship, on_delete=models.DO_NOTHING, related_name='internship_of_%(class)s')

    class Meta:
        verbose_name_plural = "Postulations"

    def __str__(self):
        return f"{self.postulant.user.username}"


     