from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Departement, Etudient, Note
from .serializers import DepartementSerializer, EtudientSerializer, NoteSerializer

class EtudientListCreateView(generics.ListCreateAPIView):
    queryset = Etudient.objects.all()
    serializer_class = EtudientSerializer

class EtudientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etudient.objects.all()
    serializer_class = EtudientSerializer

class DepartementListCreateView(generics.ListCreateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

class DepartementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

class EtudientNotesView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        etudient_id = self.kwargs['etudient_id']
        # etudient = get_object_or_404(Etudient, id=etudient_id)
        return Note.objects.filter(etudient_id=get_object_or_404(Etudient, id=etudient_id).id, matiere__publier=True)