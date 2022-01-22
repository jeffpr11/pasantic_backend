from user.auth.serializers import AuthUserSerializer, UserCredentialsSerializer
from user.models import Intern
from rest_framework.authtoken.models import Token
from rest_framework import exceptions


class AuthService:

    def get_user_by_credentials(self, data):
        serializer = UserCredentialsSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

        try:
            profile = Intern.objects.get(user__username=username)
            if profile.user.check_password(password):
                return profile
            raise exceptions.AuthenticationFailed(detail="Credenciales incorrectas.")
        except Intern.DoesNotExist:
            raise exceptions.AuthenticationFailed(detail="No existe usuario.")

    def generate_auth_token(self, member: Member):
        try:
            token, _ = Token.objects.get_or_create(user=member)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed()
        serializer = AuthUserSerializer(token)
        return serializer.data
