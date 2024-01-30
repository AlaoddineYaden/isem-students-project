from rest_framework import generics
from .models import Departement, Etudient
from .serializers import DepartementSerializer, EtudientSerializer

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