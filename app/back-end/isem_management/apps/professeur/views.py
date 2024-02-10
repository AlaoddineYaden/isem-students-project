from rest_framework.response import Response
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from ..etudient.serializers import EtudientSerializer, MatiereSerializer
from ..etudient.models import Etudient, Matiere, Note
from .models import Professeur, Enseigner
from django.db.models import Q
from django.http import JsonResponse



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
        # students = Etudient.objects.filter (filiere__module__matiere=matiere),Q(filiere__module__professeur=professor) 
        students_with_notes = []
        for student in students:
            notes = Note.objects.filter(etudient=student, matiere=matiere)
            student_info = {
                'student_name': f"{student.user.first_name} {student.user.last_name}",
                'notes': [{'note_type': note.note_type, 'note': note.note} for note in notes]
            }
            students_with_notes.append(student_info)
        print(students_with_notes)
        return Response(students_with_notes)

class ProfesseurMatieresView(generics.ListAPIView):
    serializer_class = MatiereSerializer

    def get_queryset(self):
        professor_id = self.kwargs['professor_id']
        professor = get_object_or_404(Professeur, pk=professor_id)
        subjects_taught = Enseigner.objects.filter(professeur=professor).values_list('matiere__id', flat=True)
        # Get the details of all those subjects
        matieres = Matiere.objects.filter(id__in=subjects_taught)

        return matieres