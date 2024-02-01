from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from ..etudient.serializers import EtudientSerializer
from ..etudient.models import Etudient,Matiere
from .models import Professeur, Enseigner
# Create your views here.


####### neeed to be fixed
class ProfesseurEtudientsView(generics.ListAPIView):
    serializer_class = EtudientSerializer
    def get_queryset(self):
        professor_id = self.kwargs['professor_id']
        matiere_id = self.kwargs['matiere_id']
        professor = get_object_or_404(Professeur, pk=professor_id)
        matiere = get_object_or_404(Matiere, pk=matiere_id)

        # Check if the professor teaches the specified subject
        enseigner_entry = get_object_or_404(Enseigner, professeur=professor, matiere=matiere)

        # Get all students who study the specified subject
        students = Etudient.objects.filter(filiere__module__matiere=matiere)
            # Now, you can get all students studying the specified Matiere taught by the professor
        
        return students