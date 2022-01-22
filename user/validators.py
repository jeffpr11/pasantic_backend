from rest_framework import exceptions
from django.core.exceptions import ValidationError


def username_valid(value: str):
    if not value or len(value) == 0:
        raise exceptions.AuthenticationFailed(detail="Usuario es requerido.")


def password_valid(value: str):
    if not value or len(value) == 0:
        raise exceptions.AuthenticationFailed(detail="Contraseña es requerida.")
