from rest_framework import serializers
from .models import Departement, Etudient, Filiere, Matiere, Module, Note
from django.contrib.auth.models import User


class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'first_name', 'last_name')

class EtudientSerializer(serializers.ModelSerializer):
    filiere = FiliereSerializer()
    # user = UserSerializer()
    nom = serializers.CharField(source='user.last_name')
    prenom = serializers.CharField(source='user.first_name')
    email = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Etudient
        
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = '__all__'
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

