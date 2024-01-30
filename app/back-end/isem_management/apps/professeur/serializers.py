from rest_framework import serializers
from .models import Enseigner,Professeur



class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = '__all__'

class EnseignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseigner
        fields = '__all__'