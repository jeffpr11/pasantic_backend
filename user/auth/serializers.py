from user.validators import password_valid, username_valid
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from user.serializers import AgentSerializer, InternSerializer


class AuthUserSerializer(serializers.ModelSerializer):

    token = serializers.CharField(read_only=True, source='key')
    user = InternSerializer(read_only=True)

    class Meta:
        model = Token
        fields = [
            'token',
            'user'
        ]


class UserCredentialsSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[username_valid])
    password = serializers.CharField(validators=[password_valid])
