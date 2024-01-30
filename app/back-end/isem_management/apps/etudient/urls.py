from django.urls import path
from .views import DepartementListCreateView, DepartementRetrieveUpdateDestroyView, EtudientListCreateView, EtudientRetrieveUpdateDestroyView

urlpatterns = [
    path('etudiants/', EtudientListCreateView.as_view(), name='etudient-list-create'),
    path('etudiants/<int:pk>/', EtudientRetrieveUpdateDestroyView.as_view(), name='etudient-retrieve-update-destroy'),
     path('departements/', DepartementListCreateView.as_view(), name='departement-list-create'),
    path('departements/<int:pk>/', DepartementRetrieveUpdateDestroyView.as_view(), name='departement-retrieve-update-destroy'),
]
