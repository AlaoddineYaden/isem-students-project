from django.urls import path
from .views import DepartementListCreateView, DepartementRetrieveUpdateDestroyView, EtudientListCreateView, EtudientNotesView, EtudientRetrieveUpdateDestroyView

urlpatterns = [
    path('etudiants/', EtudientListCreateView.as_view(), name='etudiant-list-create'),
    path('etudiants/<int:pk>/', EtudientRetrieveUpdateDestroyView.as_view(), name='etudiant-retrieve-update-destroy'),
    path('etudiants/<int:etudient_id>/notes/', EtudientNotesView.as_view(), name='etudiant-notes'),
    # path('departements/', DepartementListCreateView.as_view(), name='departement-list-create'),
    # path('departements/<int:pk>/', DepartementRetrieveUpdateDestroyView.as_view(), name='departement-retrieve-update-destroy'),
]
