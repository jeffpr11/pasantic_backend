from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from utils.models import *


class Agent(BaseModel):
    card_id = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=13)
    user = models.OneToOneField(
        User, on_delete=models.DO_NOTHING, related_name='profile_of_%(class)s')

    class Meta:
        indexes = [models.Index(fields=["card_id"], name="card index agent")]

    def __str__(self):
        return f"{self.card_id} {self.user.first_name}"

    @property
    def user_data(self):
        res = {'data': 'Error', 'success': False}
        try:
            user = User.objects.get(id=self.user.id)
            res = {
                'data': {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "username": user.username
                },
                'success': True}
            return res["data"]
        except User.DoesNotExist:
            return res


class Intern(BaseModel):
    born_date = models.DateField(auto_now=False)
    address = models.CharField(max_length=30)
    bio = models.TextField(max_length=500, blank=True)
    institution = models.CharField(max_length=100)
    study_field = models.CharField(max_length=100)

    # [certificado,..., certificado]
    certifications = ArrayField(models.CharField(max_length=15),
                                size=5, blank=True, null=True)

    # [idioma,..., idioma]
    languages = ArrayField(models.CharField(max_length=15),
                           size=3, blank=True, null=True)

    # [[nombre, correo],..., [nombre, correo]]
    references = ArrayField(ArrayField(models.CharField(max_length=100),
                                       size=2), size=5, blank=True, null=True)

    friends = models.ManyToManyField('self', blank=True)
    card_id = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=13)
    user = models.OneToOneField(
        User, on_delete=models.DO_NOTHING, related_name='profile_of_%(class)s')

    class Meta:
        indexes = [models.Index(fields=["card_id"], name="card index intern")]

    def __str__(self):
        return f"{self.card_id} {self.user.username}"

    @property
    def user_data(self):
        res = {'data': 'Error', 'success': False}
        try:
            user = User.objects.get(id=self.user.id)
            res = {
                'data': {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "username": user.username
                },
                'success': True}
            return res["data"]
        except User.DoesNotExist:
            return res
