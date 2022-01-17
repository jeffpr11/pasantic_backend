from rest_framework import serializers
from .models import *


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = '_all_'



class PostulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulation
        fields = '_all_'