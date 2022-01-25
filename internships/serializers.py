from rest_framework import serializers
from .models import *


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = [
            "id",
            "name",
            "description",
            "type_of_workDay",
            "requirements",
            "challenges",
            "profile",
            "start_date",
            "end_date",
            "duration_months",
            "remuneration",
            "have_remuneration",
            "owner_enterprise",
            "enterprise",
            "postulants"
        ]



class PostulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulation
        fields = [
            "id",
            "state",
            "postulant",
            "internship",
            "internship_data"
        ]