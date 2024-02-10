from django.urls import path
from .views import ProfesseurEtudientsView, ProfesseurMatieresView

urlpatterns = [
        path('professors/<int:professor_id>/matieres/<int:matiere_id>/etudiants/', ProfesseurEtudientsView.as_view(), name='etudients-de-professeur'),
        path('professors/<int:professor_id>/matieres/', ProfesseurMatieresView.as_view(), name='matiere-de-professeur'),
]
