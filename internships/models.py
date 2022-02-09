from django.db import models

from django.contrib.postgres.fields import ArrayField
from utils.models import *


class Internship(BaseModel):
    TELETRABAJO = 'T'
    PRESENCIAL = 'P'
    HIBRIDO = 'H'
    WORKDAY = [
        (TELETRABAJO, 'Teletrabajo'),
        (PRESENCIAL, 'Presencial'),
        (HIBRIDO, 'Hibrido'),
    ]

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=60, blank=True)
    type_of_workDay = models.CharField(max_length=1, choices=WORKDAY, default=TELETRABAJO)
    requirements = ArrayField(models.CharField(max_length=100), size=5, blank=True, null=True)
    challenges = ArrayField(models.CharField(max_length=100), size=5, blank=True, null=True)
    profile = models.CharField(max_length=20)
    start_date = models.DateField(auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False, blank=True, null=True)
    duration_months = models.IntegerField()
    remuneration = models.DecimalField(max_digits=6, decimal_places=3)
    have_remuneration = models.BooleanField(default=False)
    owner_enterprise = models.ForeignKey("organization.Enterprise", on_delete=models.DO_NOTHING, related_name='enterprise_of_%(class)s')

    def __str__(self):
        return self.name

    @property
    def enterprise(self):
        return self.owner_enterprise.name
    
    @property
    def postulants(self):
        return Postulation.objects.filter(internship = self).values_list('postulant__id', flat=True)


class Postulation(BaseModel):
    INICIADA = 'I'
    PENDIENTE = 'P'
    RECHAZADA = 'R'
    APROBADA = 'A'
    TERMINADA = 'T'
    STATES = [
        (INICIADA, 'Iniciada'),
        (PENDIENTE, 'Pendiente'),
        (RECHAZADA, 'Rechazada'),
        (APROBADA, 'Aprobada'),
        (TERMINADA, 'Terminada'),
    ]
    
    state = models.CharField(max_length=1, choices=STATES, default=INICIADA)
    postulant = models.ForeignKey("user.Intern", on_delete=models.DO_NOTHING, related_name='profile_of_%(class)s')
    internship = models.ForeignKey(Internship, on_delete=models.DO_NOTHING, related_name='internship_of_%(class)s')

    def __str__(self):
        return f"{self.internship.name} => {self.postulant.user.username}"

    @property
    def internship_data(self):
        return {
            "name": self.internship.name,
            "enterprise": self.internship.enterprise
        }
