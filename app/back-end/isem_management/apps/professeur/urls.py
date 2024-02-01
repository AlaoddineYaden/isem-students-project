from django.urls import path
from .views import ProfesseurEtudientsView

urlpatterns = [
        path('professors/<int:professor_id>/matieres/<int:matiere_id>/etudiants/', ProfesseurEtudientsView.as_view(), name='etudients-de-professeur'),
]
