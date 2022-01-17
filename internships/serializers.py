from rest_framework import serializers
from .models import *


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = '__all__'



class PostulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulation
        fields = '__all__'