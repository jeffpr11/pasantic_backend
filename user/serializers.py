from rest_framework import serializers
from .models import *


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['email'].split('@')[0]
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = [
            'id',
            'card_id',
            'city',
            'born_date',
            'address',
            'cellphone',
            'bio',
            'institution',
            'study_field',
            'certifications',
            'languages',
            'references',
            'friends',
            'user_data'
        ]
